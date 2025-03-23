def graph_coloring(N, M, K, edges):
    graph = {i: [] for i in range(N)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * N

    def is_safe(vertex, color):
        for neighbor in graph[vertex]:
            if colors[neighbor] == color:
                return False
        return True

    def backtrack(vertex):
        if vertex == N:
            return True

        for color in range(1, K + 1):
            if is_safe(vertex, color):
                colors[vertex] = color
                if backtrack(vertex + 1):
                    return True
                colors[vertex] = 0

        return False

    if backtrack(0):
        return f"Coloring Possible with {K} Colors\nColor Assignment: {colors}"
    else:
        return f"Coloring Not Possible with {K} Colors"

# User Input
N, M, K = map(int, input("Enter N, M, K (number of vertices, edges, colors): ").split())
edges = []
print(f"Enter {M} edges (u v):")
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))

# Output result
print(graph_coloring(N, M, K, edges))
