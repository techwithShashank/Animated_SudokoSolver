import tkinter as tk
import time

# Sudoku Solver function with animation
def solve_sudoku(grid, canvas, delay=100):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        update_canvas(canvas, i, j, num, "green")
                        canvas.update()
                        canvas.after(delay)  # Add delay for animation
                        
                        if solve_sudoku(grid, canvas, delay):
                            return True
                        
                        # Backtrack
                        grid[i][j] = 0
                        update_canvas(canvas, i, j, "", "red")
                        canvas.update()
                        canvas.after(delay)
                return False
    return True

# Function to check if a number can be placed in the Sudoku grid
def is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

# Function to update the canvas with new numbers or colors
def update_canvas(canvas, row, col, num, color):
    x1, y1 = col * 50 + 2, row * 50 + 2
    x2, y2 = x1 + 46, y1 + 46
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    canvas.create_text(x1 + 23, y1 + 23, text=str(num), font=("Arial", 18), fill="white" if color == "green" else "black")

# Main function to initialize the GUI and start solving
def main():
    root = tk.Tk()
    root.title("Sudoku Solver Animation")
    
    canvas = tk.Canvas(root, width=450, height=450, bg="white")
    canvas.pack()

    # Draw grid lines
    for i in range(0, 451, 50):
        canvas.create_line(i, 0, i, 450, width=2)
        canvas.create_line(0, i, 450, i, width=2)

    # Example Sudoku puzzle (0 represents empty cells)
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    # Fill the initial numbers on the canvas
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                update_canvas(canvas, i, j, grid[i][j], "blue")

    # Solve the Sudoku
    solve_sudoku(grid, canvas)
    root.mainloop()

if __name__ == "__main__":
    main()
