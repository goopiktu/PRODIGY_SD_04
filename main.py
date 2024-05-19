import tkinter as tk
from tkinter import messagebox

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

def display_board(board, labels):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                labels[i][j].config(text=str(board[i][j]))
            else:
                labels[i][j].config(text="")

def solve_sudoku():
    if solve(board):
        display_board(board, labels)
        messagebox.showinfo("Success", "Sudoku Solved!")
    else:
        messagebox.showerror("Error", "No solution exists")

root = tk.Tk()
root.title("Sudoku Solver")

labels = [[None for _ in range(9)] for _ in range(9)]

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    for j in range(9):
        label = tk.Label(frame, text="", width=4, height=2, font=("Arial", 18), borderwidth=2, relief="solid")
        label.grid(row=i, column=j)
        labels[i][j] = label

display_board(board, labels)

solve_button = tk.Button(root, text="Solve Sudoku", command=solve_sudoku)
solve_button.pack()

root.mainloop()
