

## Sudoku puzzle solver

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
The board variable represents the Sudoku puzzle as a list of lists. Each inner list represents a row, and the numbers represent the values in each cell. Zero (0) indicates an empty cell.

def solve(bo):
    find = find_empty_grid(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False

The solve function takes the Sudoku board bo as input and implements a recursive backtracking algorithm to solve the puzzle.
It first calls the find_empty_grid function to find the next empty cell in the puzzle.
If no empty cells are found (find is None), it means the puzzle is solved, so it returns True.
Otherwise, it assigns the coordinates of the empty cell to row and col.
It then iterates over numbers 1 to 9 and checks if each number is valid in the current cell using the is_valid function.
If a number is valid, it assigns that number to the current cell (bo[row][col] = i) and recursively calls the solve function again.
If the recursive call returns True, it means the puzzle is solved, so it returns True.
If the recursive call returns False, it means the current number choice didn't lead to a solution, so it backtracks by assigning 0 to the current cell (bo[row][col] = 0) and continues with the next number.
If none of the numbers lead to a solution, it returns False.

def is_valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

The is_valid function checks if a given number num is valid in a particular position pos in the Sudoku board bo.
It checks for three conditions: same number in the same row, same number in the same column, and same number in the same 3x3 grid box.
The first two loops iterate over each cell in the same row and column as the current position, checking if any of them contain the same number. If a duplicate number is found, the function returns False.
The next two loops determine the 3x3 grid box that the current position belongs to. It iterates over each cell in that grid box, checking for any duplicate number. If a duplicate number is found, the function returns False.
If no duplicate numbers are found, the function returns True, indicating that the number is valid in the given position.

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


The print_board function takes the Sudoku board bo as input and prints it in a visually appealing format.
It uses nested loops to iterate over each cell in the board.
The outer loop iterates over each row, and the inner loop iterates over each column.
It checks if the current row index is a multiple of 3 and not equal to 0, indicating the end of a 3x3 grid box. If true, it prints a line of dashes to separate the grid boxes.
It checks if the current column index is a multiple of 3 and not equal to 0, indicating the end of a column within a grid box. If true, it prints a vertical bar (|) to separate the columns.
It then prints the value of the current cell bo[i][j].
If it's the last cell in the row (column index 8), it prints the value without a space and adds a line break.
Otherwise, it prints the value followed by a space.
The function outputs the Sudoku board in a grid-like format.
python


def find_empty_grid(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None


The find_empty_grid function takes the Sudoku board bo as input and searches for an empty cell (value 0) in the board.
It uses nested loops to iterate over each cell in the board.
If an empty cell is found (bo[i][j] == 0), it immediately returns the coordinates (i, j) as a tuple representing the row and column.
If no empty cells are found after iterating through the entire board, it returns None.
The code starts by defining the Sudoku puzzle board, and then the solve function is called to solve the puzzle using a recursive backtracking algorithm. The is_valid function is used to check the validity of numbers in each position, and the print_board function is used to display the puzzle board in a readable format. The find_empty_grid function is used to find the next empty cell in the puzzle during the solving process