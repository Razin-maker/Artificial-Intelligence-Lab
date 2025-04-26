import random

# Step 1: Generate random points and centers
points = [(random.randint(0, 19), random.randint(0, 19)) for _ in range(100)]
centers = [(random.randint(0, 19), random.randint(0, 19)) for _ in range(10)]

# Print generated points
print("\nGenerated Points (x, y):")
for i, p in enumerate(points):
    print(f"P{i:02d}: {p}", end='  ')
    if (i + 1) % 5 == 0:  # 5 points per line
        print()
print("\n")

# Print initial cluster centers clearly
print("Initial Cluster Centers (Before Clustering):")
for i, c in enumerate(centers):
    print(f"Center {i}: {c}")
print("\n")

# Step 2: Define Manhattan distance
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Step 3: Assign points to the nearest center
assignments = []
for p in points:
    min_dist = float('inf')
    assigned_cluster = -1
    for i, c in enumerate(centers):
        d = manhattan_distance(p, c)
        if d < min_dist:
            min_dist = d
            assigned_cluster = i
    assignments.append(assigned_cluster)

# Step 4: Update centers based on assignments
new_centers = [(0, 0)] * len(centers)
counts = [0] * len(centers)

for idx, cluster_id in enumerate(assignments):
    x, y = points[idx]
    cx, cy = new_centers[cluster_id]
    new_centers[cluster_id] = (cx + x, cy + y)
    counts[cluster_id] += 1

for i in range(len(new_centers)):
    if counts[i] != 0:
        cx, cy = new_centers[i]
        new_centers[i] = (cx // counts[i], cy // counts[i])

centers = new_centers

# Print updated centers
print("Updated Cluster Centers (After Assignment):")
for i, c in enumerate(centers):
    print(f"Center {i}: {c}")
print("\n")

# Step 5: Visualization using print()

# Create empty 20x20 grid
grid = [['.' for _ in range(20)] for _ in range(20)]

# Place centers
for cx, cy in centers:
    if 0 <= cx < 20 and 0 <= cy < 20:
        grid[cy][cx] = 'C'

# Place points
for idx, (px, py) in enumerate(points):
    if 0 <= px < 20 and 0 <= py < 20:
        if grid[py][px] == '.':
            grid[py][px] = 'P'

# Print the grid (from top to bottom)
print("2D Grid Visualization :\n")
for row in grid[::-1]:  # start from top
    print(' '.join(row))
