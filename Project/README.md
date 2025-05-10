# 🧩 Puzzle Solver

This Python project simulates two classic AI problem-solving environments: the **8-Puzzle Game** and the **Tower of Hanoi**, implementing search-based algorithms such as **BFS**, **DFS**, and **IDDFS** to find optimal solutions.

## 🚀 Features

### 8-Puzzle Game
- Automatically generates a random solvable 8-puzzle state.
- Solves using:
  - **Breadth-First Search (BFS)**
  - **Depth-First Search (DFS)**
  - **Iterative Deepening Depth-First Search (IDDFS)**
- Displays each move (UP, DOWN, LEFT, RIGHT) with matrix state step-by-step.
- Compares algorithm performance (moves, time, nodes expanded).

### Tower of Hanoi
- Simulates Tower of Hanoi puzzle with 3 disks (Disk 1, Disk 2, Disk 3).
- Recursive solution with step-by-step visualization.
- Shows disk moves between pegs ("Move Disk 1 from A to C").
- Displays total steps taken and time consumed.

## 📊 Algorithms Used
- **BFS:** Explores all nodes at a level before going deeper.
- **DFS:** Explores as far as possible before backtracking.
- **IDDFS:** Combines the benefits of DFS and BFS by using iterative depth limits.

## 📦 Requirements
- Python 3.x
