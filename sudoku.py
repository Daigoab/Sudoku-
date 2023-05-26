
#Lists within a list 'board' containing the Soduko puzzle
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
    #Call the find_empty_grid to find empty cells represnted by zero
    find = find_empty_grid(bo)
    #If an empty cell is not found the number has already been filled so puzzle solved
    if not find:
        return True
    #Assigns the variables to empty cells found
    else:
        row, col = find
    #The loop iterates values 1 to 10 that could be the possible values of empty cell
    for i in range (1, 10):
        #The number is checked if valid by calling is_valid
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i
            #If value is valid, the number is placed and the solve function called to solve the remaining empty cell
            if solve (bo):
                return True
            #If not valid we assign it 0
            bo[row][col] = 0
    #Loop continues to next value if invalid
    return False

def is_valid (bo, num, pos):  #Pos representing position row and column as input

        # Checks if a value 'num' is in the same row except in the current column 'pos[1]' 
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            #If a duplicate is found num is invalid 
            return False

    # Checks if a value 'num' is in the same column  except in the current row 'pos[0]'
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Checks if a value 'num' is in the same grid box as in the current cell 'pos'
    box_x = pos[1] // 3   #Calculates current position of grid based on the column 'pos[1]'  
    box_y = pos[0] // 3   #Based on current row 'pos[0]'

    #Loop iterates over all the cells in the grid box except in current cell 'pos'
    for i in range(box_y*3, box_y*3 + 3): 
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                #If found the number is invalid
                return False
    #If not found num is valid        
    return True


def print_board(bo):
    #Loop iterates over the range of length of the board
    for i in range(len(bo)):
        #Checks if current row index is a multiple of 3 and is not equal to 0
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        #Loop iterates over the range of the length of bo[0] to give number of columns
        for j in range(len(bo[0])):
            #Checks if the current column index is a multiple of 3 and is not equal to
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            #Prints value of current cell 'bo[i][j]'
            if j == 8:
                print(bo[i][j])
            #Checks if it is the last cell in the row (column index 8) then it prints the value without a space and adds a line break
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty_grid(bo):
    #Loop iterates over each row
    for i in range(len(bo)):
        #Loop iterates over each column
        for j in range(len(bo[0])):
            #Checks if the value of the current cell 'bo[i][j]' is equal to 0
            if bo[i][j] == 0:
                #If an empty cell is found, it immediately returns the coordinates (i, j) as a tuple 
                return (i, j)  # row, col
    #If no empty cells are found
    return None
                

print_board(board)
solve(board)
print("------------------------")
print("The solved Sudoku: ")
print_board(board)
