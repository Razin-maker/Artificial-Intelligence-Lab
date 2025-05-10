import time
import random
from collections import deque

# ===================== 8‑Puzzle: Solvable State Generation =====================

def is_solvable(state, size=3):
    inv_count = 0
    lst = [x for x in state if x != 0]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                inv_count += 1
    return inv_count % 2 == 0

def generate_random_state(size=3):
    state = list(range(size*size))
    while True:
        random.shuffle(state)
        if is_solvable(state, size):
            return tuple(state)

# ===================== 8‑Puzzle Neighbor Generation (with Moves) =====================

def get_neighbors_puzzle(state, size=3):
    """
    Returns list of (neighbor_state, move) where move is one of 'Up','Down','Left','Right'.
    """
    neighbors = []
    zero = state.index(0)
    r, c = divmod(zero, size)
    directions = [(-1,0,'Up'), (1,0,'Down'), (0,-1,'Left'), (0,1,'Right')]
    for dr, dc, move in directions:
        nr, nc = r+dr, c+dc
        if 0 <= nr < size and 0 <= nc < size:
            ni = nr*size + nc
            s = list(state)
            s[zero], s[ni] = s[ni], s[zero]
            neighbors.append((tuple(s), move))
    return neighbors

# ===================== Tower of Hanoi Neighbor Generation =====================

def get_neighbors_hanoi(state):
    """
    Returns list of (neighbor_state, move) where move describes disk and pegs.
    """
    neighbors = []
    for i in range(3):
        if not state[i]: continue
        disk = state[i][-1]
        for j in range(3):
            if i != j and (not state[j] or state[j][-1] > disk):
                new_pegs = [list(peg) for peg in state]
                new_pegs[j].append(new_pegs[i].pop())
                move = f"Move disk{disk} from peg{i+1} to peg{j+1}"
                neighbors.append((tuple(tuple(peg) for peg in new_pegs), move))
    return neighbors

# ===================== Search Algorithms =====================

def bfs_solver(initial, goal, get_neighbors):
    start = time.time()
    frontier = deque([initial])
    parent = {initial: (None, None)}  # state -> (parent_state, move)
    nodes = 0
    while frontier:
        s = frontier.popleft()
        nodes += 1
        if s == goal:
            # reconstruct path and moves
            path, moves = [], []
            cur = s
            while cur is not None:
                p, m = parent[cur]
                path.append(cur)
                moves.append(m)
                cur = p
            path.reverse(); moves.reverse()
            return path, moves[1:], nodes, time.time() - start
        for nbr, move in get_neighbors(s):
            if nbr not in parent:
                parent[nbr] = (s, move)
                frontier.append(nbr)
    return None, None, nodes, time.time() - start

def dfs_solver(initial, goal, get_neighbors, max_depth):
    start = time.time()
    nodes = [0]
    parent = {initial: (None, None)}
    found = [None]

    def dfs(s, depth):
        nodes[0] += 1
        if s == goal:
            found[0] = s
            return True
        if depth == 0:
            return False
        for nbr, move in get_neighbors(s):
            if nbr not in parent:
                parent[nbr] = (s, move)
                if dfs(nbr, depth-1):
                    return True
        return False

    if not dfs(initial, max_depth):
        return None, None, nodes[0], time.time() - start
    path, moves = [], []
    cur = found[0]
    while cur is not None:
        p, m = parent[cur]
        path.append(cur)
        moves.append(m)
        cur = p
    path.reverse(); moves.reverse()
    return path, moves[1:], nodes[0], time.time() - start

def iddfs_solver(initial, goal, get_neighbors, max_depth):
    start = time.time()
    total = 0
    for depth in range(1, max_depth+1):
        parent = {initial: (None, None)}
        nodes = [0]
        def dls(s, d):
            nodes[0] += 1
            if s == goal:
                return True
            if d == 0:
                return False
            for nbr, move in get_neighbors(s):
                if nbr not in parent:
                    parent[nbr] = (s, move)
                    if dls(nbr, d-1):
                        return True
            return False
        if dls(initial, depth):
            path, moves = [], []
            cur = goal
            while cur is not None:
                p, m = parent[cur]
                path.append(cur)
                moves.append(m)
                cur = p
            path.reverse(); moves.reverse()
            return path, moves[1:], total + nodes[0], time.time() - start
        total += nodes[0]
    return None, None, total, time.time() - start

# ===================== Performance Comparison =====================

def compare_algorithms(initial, goal, get_neighbors, max_depth):
    results = {}
    print("\nComparing BFS...")
    results['BFS'] = bfs_solver(initial, goal, get_neighbors)
    print("Comparing DFS...")
    results['DFS'] = dfs_solver(initial, goal, get_neighbors, max_depth)
    print("Comparing IDDFS...")
    results['IDDFS'] = iddfs_solver(initial, goal, get_neighbors, max_depth)
    print("\n--- Comparison Results ---")
    for name, (path, moves, nodes, t) in results.items():
        if path:
            print(f"{name}: moves={len(path)-1}, nodes={nodes}, time={t:.4f}s")
        else:
            print(f"{name}: no solution")
    solved = {n:r for n,r in results.items() if r[0]}
    if solved:
        best = min(solved.items(), key=lambda kv: len(kv[1][0])-1)
        print(f"\n🏆 Best: {best[0]} in {len(best[1][0])-1} moves")
    else:
        print("\n❌ No algorithm solved it.")

# ===================== Main Program =====================

def main():
    print("Puzzle Solver")
    print("=======================")
    print("1) 8‑Puzzle (3×3)")
    print("2) Tower of Hanoi")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        size = 3
        goal = tuple(range(1, size*size)) + (0,)
        initial = generate_random_state(size)
        get_nbrs = lambda s: get_neighbors_puzzle(s, size)
        print("\nInitial 8‑Puzzle:")
        for i in range(size): print(initial[i*size:(i+1)*size])
        print("\nGoal:")
        for i in range(size): print(goal[i*size:(i+1)*size])
    elif choice == "2":
        n = int(input("Enter number of disks: ").strip())
        initial = (tuple(range(n,0,-1)), (), ())
        goal = ((), (), tuple(range(n,0,-1)))
        get_nbrs = get_neighbors_hanoi
        print("\nInitial Tower State:")
        for pi,peg in enumerate(initial,1): print(f" Peg {pi}: {[f'disk{d}' for d in peg]}")
        print("\nGoal:")
        for pi,peg in enumerate(goal,1): print(f" Peg {pi}: {[f'disk{d}' for d in peg]}")
    else:
        print("Invalid"); return

    print("\nSelect Algorithm:")
    print("1) BFS")
    print("2) DFS (with max depth)")
    print("3) IDDFS (with max depth)")
    print("4) Compare Performance")
    algo = input("Choice (1–4): ").strip()
    md = None
    if algo in ["2","3","4"]:
        md = int(input("Enter max depth: ").strip())

    if algo == "4":
        compare_algorithms(initial, goal, get_nbrs, md)
        return

    print("\nRunning...")
    if algo == "1": sol, moves, nodes, t = bfs_solver(initial, goal, get_nbrs); name="BFS"
    elif algo == "2": sol, moves, nodes, t = dfs_solver(initial, goal, get_nbrs, md); name="DFS"
    elif algo == "3": sol, moves, nodes, t = iddfs_solver(initial, goal, get_nbrs, md); name="IDDFS"
    else: print("Invalid"); return

    print(f"\n{name} Results:")
    if not sol:
        print(" No solution.")
    else:
        for i,(st,mv) in enumerate(zip(sol, [None]+moves)):
            print(f"Step {i}: Move: {mv}" if mv else f"Step {i}: Start")
            if choice == "1":
                for r in range(size): print(st[r*size:(r+1)*size])
            else:
                for pi,peg in enumerate(st,1): print(f" Peg {pi}: {[f'disk{d}' for d in peg]}")
            print("---")
        print(f"Moves: {len(sol)-1}")
    print(f"Nodes expanded: {nodes}")
    print(f"Time: {t:.4f}s")

if __name__ == "__main__":
    main()