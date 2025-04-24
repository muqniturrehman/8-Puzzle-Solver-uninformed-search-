# 8-Puzzle Solver using Uninformed Search Algorithms

This project implements classic uninformed search algorithms to solve the 8-puzzle problem. The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with 8 numbered tiles and one empty space. The objective is to move the tiles around to reach a specific goal state from a given starting configuration.

## Features

- Solves the 8-puzzle using the following algorithms:
  - Backtracking
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
  - Depth-First Iterative Deepening (DFID)

## Example

**Start State:**
```
4 7 8  
3 6 5  
1 2   
```

**Goal State:**
```
1 2 3  
4 5 6  
7 8   
```

## How It Works

Each algorithm explores possible moves of the empty space (up, down, left, right) to generate new states. These states are traversed based on the search strategy to find a path to the goal state.

- DFS and Backtracking explore deep paths first.
- BFS explores level by level.
- DFID gradually increases depth to combine the benefits of DFS and BFS.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository.
3. Run the script with:

```bash
python lab-1.py
```

4. In the `main()` function, uncomment the algorithm you want to run:

```python
# solver.solve_puzzle_backtracking()
# solver.solve_puzzle_dfs()
# solver.solve_puzzle_bfs()
solver.solve_puzzle_dfid()
```

## Output

The script will print the step-by-step transformation from the initial state to the goal state, including each move taken.

## Author

**Muqnit Ur Rehman**
