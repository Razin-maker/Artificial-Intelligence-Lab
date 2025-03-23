def iddfs(maze, start, target):
    rows, cols = len(maze), len(maze[0])

    def is_valid_move(x, y, visited):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 and (x, y) not in visited

    def dls(node, depth, visited, path):
        if depth == 0:
            return node == target
        if depth > 0:
            x, y = node
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if is_valid_move(nx, ny, visited):
                    visited.add((nx, ny))
                    path.append((nx, ny))
                    if dls((nx, ny), depth - 1, visited, path):
                        return True
                    path.pop()
                    visited.remove((nx, ny))
        return False

    for depth in range(rows * cols):
        visited = set()
        visited.add(start)
        path = [start]
        if dls(start, depth, visited, path):
            return f"Path found at depth {depth} using IDDFS\nTraversal Order: {path}"

    return "No path found"

rows, cols = map(int, input("Enter maze dimensions (rows cols): ").split())
print("Enter maze row by row (0 for empty, 1 for wall):")
maze = [list(map(int, input().split())) for _ in range(rows)]
start = tuple(map(int, input("Enter start cell (row col): ").split()))
target = tuple(map(int, input("Enter target cell (row col): ").split()))

print(iddfs(maze, start, target))
