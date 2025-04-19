import time
import random
from collections import deque

# ===================== Solvable State Generation =====================

def is_solvable(state, size=3):
    inv_count = 0
    state_list = [num for num in state if num != 0]
    for i in range(len(state_list)):
        for j in range(i + 1, len(state_list)):
            if state_list[i] > state_list[j]:
                inv_count += 1
    return inv_count % 2 == 0

def generate_random_state(size=3):
    state = list(range(size * size))
    while True:
        random.shuffle(state)
        if is_solvable(state, size):
            return tuple(state)

# ===================== Puzzle Neighbors =====================

def get_neighbors_puzzle(state, size=3):
    neighbors = []
    zero_index = state.index(0)
    r, c = divmod(zero_index, size)
    moves = []
    if r > 0: moves.append((-1, 0))
    if r < size - 1: moves.append((1, 0))
    if c > 0: moves.append((0, -1))
    if c < size - 1: moves.append((0, 1))
    for dr, dc in moves:
        new_r, new_c = r + dr, c + dc
        new_index = new_r * size + new_c
        new_state = list(state)
        new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
        neighbors.append(tuple(new_state))
    return neighbors

# ===================== Search Algorithms =====================

def bfs_solver(initial, goal, get_neighbors):
    start_time = time.time()
    frontier = deque([initial])
    parent = {initial: None}
    nodes_expanded = 0
    while frontier:
        state = frontier.popleft()
        nodes_expanded += 1
        if state == goal:
            end_time = time.time()
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return list(reversed(path)), nodes_expanded, end_time - start_time
        for neighbor in get_neighbors(state):
            if neighbor not in parent:
                parent[neighbor] = state
                frontier.append(neighbor)
    return None, nodes_expanded, time.time() - start_time

def dfs_solver(initial, goal, get_neighbors, max_depth):
    start_time = time.time()
    nodes_expanded = [0]
    parent = {initial: None}
    found = [None]

    def dfs_recursive(state, depth):
        nodes_expanded[0] += 1
        if state == goal:
            found[0] = state
            return True
        if depth == 0:
            return False
        for neighbor in get_neighbors(state):
            if neighbor not in parent:
                parent[neighbor] = state
                if dfs_recursive(neighbor, depth - 1):
                    return True
        return False

    success = dfs_recursive(initial, max_depth)
    if success:
        path = []
        state = found[0]
        while state is not None:
            path.append(state)
            state = parent[state]
        return list(reversed(path)), nodes_expanded[0], time.time() - start_time
    else:
        return None, nodes_expanded[0], time.time() - start_time

def iddfs_solver(initial, goal, get_neighbors, max_depth_limit):
    start_time = time.time()
    total_nodes_expanded = 0

    def dls(state, depth, parent, nodes_expanded):
        nodes_expanded[0] += 1
        if state == goal:
            return True
        if depth == 0:
            return False
        for neighbor in get_neighbors(state):
            if neighbor not in parent:
                parent[neighbor] = state
                if dls(neighbor, depth - 1, parent, nodes_expanded):
                    return True
        return False

    for depth in range(1, max_depth_limit + 1):
        parent = {initial: None}
        nodes_expanded = [0]
        if dls(initial, depth, parent, nodes_expanded):
            total_nodes_expanded += nodes_expanded[0]
            path = []
            state = goal
            while state is not None:
                path.append(state)
                state = parent[state]
            return list(reversed(path)), total_nodes_expanded, time.time() - start_time
        total_nodes_expanded += nodes_expanded[0]
    return None, total_nodes_expanded, time.time() - start_time

# ===================== Performance Comparison =====================

def compare_algorithms(initial, goal, get_neighbors, max_depth):
    results = {}

    print("\nComparing BFS...")
    bfs_path, bfs_nodes, bfs_time = bfs_solver(initial, goal, get_neighbors)
    results['BFS'] = (bfs_path, bfs_nodes, bfs_time)

    print("Comparing DFS...")
    dfs_path, dfs_nodes, dfs_time = dfs_solver(initial, goal, get_neighbors, max_depth)
    results['DFS'] = (dfs_path, dfs_nodes, dfs_time)

    print("Comparing IDDFS...")
    iddfs_path, iddfs_nodes, iddfs_time = iddfs_solver(initial, goal, get_neighbors, max_depth)
    results['IDDFS'] = (iddfs_path, iddfs_nodes, iddfs_time)

    print("\n--- Comparison Results ---")
    for name, (path, nodes, time_taken) in results.items():
        if path:
            print(f"{name}: Moves = {len(path) - 1}, Nodes Expanded = {nodes}, Time = {time_taken:.4f} sec")
        else:
            print(f"{name}: No solution found.")

    # Determine best (lowest move count)
    solved = {k: v for k, v in results.items() if v[0] is not None}
    if solved:
        best = min(solved.items(), key=lambda x: len(x[1][0]) - 1)
        print(f"\n🏆 Best Performance: {best[0]} with {len(best[1][0]) - 1} moves")
    else:
        print("\n❌ None of the algorithms found a solution.")

# ===================== Main Program =====================

def main():
    print("8-Puzzle Solver")
    print("========================")
    size = 3
    goal = tuple(range(1, size * size)) + (0,)
    initial = generate_random_state(size)

    print("\nInitial State:")
    for i in range(size):
        print(initial[i*size:(i+1)*size])

    print("\nGoal State:")
    for i in range(size):
        print(goal[i*size:(i+1)*size])

    print("\nSelect Option:")
    print("1. BFS")
    print("2. DFS (with max depth)")
    print("3. IDDFS (Iterative Deepening DFS)")
    print("4. Compare Performance")
    algo_choice = input("Enter choice (1, 2, 3, or 4): ").strip()

    if algo_choice in ["2", "3", "4"]:
        try:
            max_depth = int(input("Enter max depth for DFS/IDDFS: ").strip())
        except ValueError:
            max_depth = 50
    else:
        max_depth = None

    get_neighbors = lambda state: get_neighbors_puzzle(state, size)

    if algo_choice == "4":
        compare_algorithms(initial, goal, get_neighbors, max_depth)
        return

    print("\nRunning algorithm...")
    if algo_choice == "1":
        solution, nodes, t_taken = bfs_solver(initial, goal, get_neighbors)
        algo_name = "BFS"
    elif algo_choice == "2":
        solution, nodes, t_taken = dfs_solver(initial, goal, get_neighbors, max_depth)
        algo_name = "DFS"
    elif algo_choice == "3":
        solution, nodes, t_taken = iddfs_solver(initial, goal, get_neighbors, max_depth)
        algo_name = "IDDFS"
    else:
        print("Invalid algorithm choice.")
        return

    print("\nAlgorithm Used:", algo_name)
    if solution is None:
        print("No solution found within the given limits.")
    else:
        print("Solution found!")
        for idx, state in enumerate(solution):
            print(f"Step {idx}:")
            for i in range(size):
                print(state[i*size:(i+1)*size])
            print("---")
        print("Number of moves:", len(solution) - 1)

    print("Nodes expanded:", nodes)
    print("Time taken: {:.4f} seconds".format(t_taken))

if __name__ == "__main__":
    main()
