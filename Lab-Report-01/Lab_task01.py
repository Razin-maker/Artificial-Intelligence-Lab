import random

def generate_grid(n, free_prob=0.7):
    
    return [[1 if random.random() < free_prob else 0 for _ in range(n)] for _ in range(n)]

def print_grid(grid, source, goal, path=None):
   
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if (i, j) == source:
                print("S", end=" ")
            elif (i, j) == goal:
                print("G", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()
    print()

def dfs(grid, current, goal, visited, order):
    
    x, y = current
    visited.add(current)
    order.append(current)
    
    if current == goal:
        return [current]
    
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < len(grid) and 0 <= ny < len(grid) and 
            grid[nx][ny] == 1 and (nx, ny) not in visited):
            result = dfs(grid, (nx, ny), goal, visited, order)
            if result:
                return [current] + result
    return None

def main():
    n = random.randint(4, 7)
    grid = generate_grid(n)
    
    free_cells = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
    if len(free_cells) < 2:
        return main()  

    source = random.choice(free_cells)
    goal = random.choice(free_cells)
    while goal == source:
        goal = random.choice(free_cells)
    
    visited = set()
    order = []  
    path = dfs(grid, source, goal, visited, order)

    print("Grid (0 = obstacle, 1 = free cell, s = source, G = goal):")
    print_grid(grid, source, goal)
    print("Source:", source)
    print("Goal:", goal)
    if path:
        print("DFS Path:", path)
    else:
        print("No path found using DFS.")
    print("DFS Order of Traversal:", order)

if __name__ == "__main__":
    main()
