# Sudoku Solver

A Python-based Sudoku solver with animations using Tkinter. This project visualizes the backtracking algorithm as it solves the puzzle step-by-step.

## Features
- Solves Sudoku puzzles using backtracking.
- Visual animation of the solving and backtracking process using Tkinter.

## Time and Space Complexity

### **Time Complexity**
The time complexity of the backtracking algorithm depends on the number of empty cells in the Sudoku grid.

- **Worst Case**: O(9^(n)), where `n` is the number of empty cells.
  - For each empty cell, the algorithm tries all possible numbers (1–9), leading to a branching factor of 9.
  - If there are `n` empty cells, the total number of combinations to check is 9^n.

- **Best Case**: When the grid is almost complete, fewer branches are explored, significantly reducing the complexity.

---

### **Space Complexity**
- **Space Complexity**: O(n), where `n` is the number of empty cells.
  - The algorithm uses the call stack during recursion, with the maximum depth equal to the number of empty cells.
  - No additional data structures are used apart from the input grid.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/techwithShashank/Animated_SudokoSolver.git
