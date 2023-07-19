"""
This file contains the functions for playing sudoku, there is no need to edit this file. Import this file into your main.py file to use the functions using `import sudoku as sl`.
 _  _  ____  ____   ___    ____  ____    __    ___  _   _    ____  ____  ___  _   _ 
( )/ )(_  _)(  _ \ / __)  (_  _)( ___)  /__\  / __)( )_( )  (_  _)( ___)/ __)( )_( )
 )  (  _)(_  )(_) )\__ \    )(   )__)  /(__)\( (__  ) _ (     )(   )__)( (__  ) _ ( 
(_)\_)(____)(____/ (___/   (__) (____)(__)(__)\___)(_) (_)   (__) (____)\___)(_) (_)
"""

import random

def display_sudoku(sudoku_board):
    # Print the column numbers
    repeatCharacter(" ", 1+2)
    for i in range(9):
        print(f"{i:^3}", end=" ")
    print()

    # Top bar
    repeatCharacter(" ", 1+1)
    repeatCharacter("—", 9*4+1)
    print()
    
    for i in range(9): # Repeat each row
       
        # Print row numbers and cell wall
        print(f"{i:<{1+1}}", end="")
        print(f"|", end="")
        
        for j in range(9): # Repeat each cell
            #Print the number inside the cell and cell walls
            if sudoku_board[i][j] == 0:
                print(f"   ", end="|")
            else:
                print(f" {str(sudoku_board[i][j])} ", end="|")
        print()

        # Print bar between every row
        if i != 9-1:
            repeatCharacter(" ", 1+1)
            repeatCharacter("|———", 9)
            print("|")
        else:
            repeatCharacter(" ", 1+1)
            repeatCharacter("—", 9*4+1)
    print()

def repeatCharacter(character, amount): # Repeats a character a certain amount of times
    for i in range(amount):
        print(character, end="")

def find_empty_cell(sudoku):
    # Find and return the coordinates of the first empty cell (cell with 0 value)
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return [row, col]
    return [-1,-1]

def remove_cells(sudoku, cells_to_remove):
    # Remove random cells from the solved Sudoku
    # The number of cells to be removed can vary depending on the desired difficulty level

    for _ in range(cells_to_remove):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        sudoku[row][col] = 0
    
    return sudoku

def generate_sudoku():
    # Initialize an empty 9x9 matrix
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    # Solve the Sudoku puzzle
    solve_sudoku(sudoku)

    # Remove random cells from the solved Sudoku to create the puzzle
    remove_cells(sudoku, 40)

    return sudoku
    
def solve_sudoku(sudoku):
    # Find an empty cell in the Sudoku
    empty_cell = find_empty_cell(sudoku)
    row = empty_cell[0]
    col = empty_cell[1]

    # If all cells are filled, the Sudoku is solved
    if empty_cell == [-1, -1]:
        return sudoku

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)

    # Loop over these numbers and check it they are valid in the empty cell
    for i in range(9):
        current_guess = numbers[i]
        if is_valid_move(sudoku, row, col, current_guess):
            # Place the number in the empty cell
            sudoku[row][col] = current_guess

            # Recursively solve the Sudoku
            if (solve_sudoku(sudoku) != False):
                return sudoku

            # If the Sudoku cannot be solved, backtrack and try a different number
            sudoku[row][col] = 0
    
    return False

sudokus = [[[3, 2, 0, 9, 6, 0, 0, 0, 4], [8, 4, 1, 7, 5, 2, 3, 9, 6], [9, 5, 0, 3, 4, 8, 0, 7, 0], [0, 6, 5, 4, 1, 3, 9, 2, 8], [2, 9, 8, 5, 7, 6, 1, 4, 3], [1, 3, 4, 8, 2, 9, 7, 0, 5], [5, 7, 9, 1, 0, 4, 0, 8, 2], [6, 8, 3, 2, 9, 5, 0, 1, 7], [4, 1, 2, 6, 0, 0, 5, 3, 0]], [[4, 0, 5, 9, 0, 0, 0, 3, 0], [8, 7, 1, 0, 0, 0, 5, 6, 9], [3, 6, 9, 0, 5, 0, 0, 0, 2], [7, 0, 2, 5, 0, 4, 1, 8, 6], [5, 4, 8, 2, 6, 1, 9, 7, 3], [0, 1, 6, 8, 0, 7, 2, 5, 4], [6, 0, 0, 1, 2, 0, 3, 9, 7], [1, 9, 7, 4, 8, 3, 6, 2, 5], [2, 5, 0, 6, 7, 9, 8, 4, 1]], [[5, 0, 6, 2, 0, 4, 1, 7, 0], [0, 3, 2, 1, 7, 8, 0, 0, 9], [1, 0, 7, 0, 6, 9, 0, 3, 2], [0, 1, 3, 9, 4, 0, 8, 0, 7], [7, 5, 9, 3, 0, 2, 6, 1, 4], [8, 0, 4, 6, 0, 7, 3, 9, 5], [0, 0, 1, 8, 0, 3, 7, 0, 6], [0, 0, 0, 4, 0, 6, 2, 8, 1], [2, 0, 8, 0, 5, 1, 0, 4, 3]], [[0, 0, 4, 6, 7, 2, 0, 0, 5], [2, 0, 0, 8, 9, 0, 4, 3, 0], [5, 0, 0, 0, 0, 3, 7, 2, 6], [0, 0, 7, 0, 5, 0, 1, 4, 0], [9, 5, 1, 3, 6, 0, 2, 0, 0], [4, 2, 8, 0, 0, 7, 0, 5, 3], [1, 6, 0, 4, 8, 9, 3, 0, 2], [8, 0, 2, 0, 3, 6, 0, 1, 0], [7, 4, 3, 5, 2, 1, 9, 6, 8]], [[0, 0, 0, 8, 4, 0, 1, 7, 5], [0, 8, 4, 0, 9, 7, 0, 0, 6], [3, 0, 1, 2, 6, 0, 4, 0, 0], [0, 9, 2, 6, 5, 0, 7, 0, 8], [7, 5, 3, 9, 2, 8, 6, 0, 0], [0, 1, 0, 7, 0, 0, 0, 0, 0], [0, 6, 0, 4, 7, 9, 8, 1, 3], [1, 4, 9, 3, 8, 0, 5, 6, 7], [8, 3, 0, 0, 0, 6, 2, 0, 4]], [[4, 0, 9, 3, 2, 5, 6, 7, 0], [5, 1, 7, 8, 0, 0, 3, 0, 0], [2, 3, 0, 7, 9, 0, 0, 4, 0], [0, 6, 0, 1, 8, 0, 0, 2, 0], [7, 4, 8, 0, 0, 0, 0, 6, 0], [1, 0, 0, 6, 0, 7, 9, 0, 0], [6, 0, 0, 0, 0, 3, 8, 0, 0], [8, 0, 1, 4, 7, 9, 2, 0, 0], [3, 0, 2, 0, 0, 0, 4, 1, 7]], [[0, 5, 8, 0, 4, 0, 6, 1, 7], [0, 7, 9, 1, 8, 5, 4, 3, 0], [0, 1, 0, 6, 0, 0, 0, 0, 0], [9, 0, 5, 3, 0, 0, 0, 7, 8], [0, 0, 0, 0, 0, 0, 0, 9, 0], [8, 3, 0, 0, 5, 0, 2, 6, 0], [1, 8, 6, 5, 0, 2, 0, 0, 3], [3, 0, 0, 0, 0, 0, 9, 0, 1], [0, 0, 0, 4, 3, 0, 0, 2, 0]], [[0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 9, 6, 2, 0, 0], [6, 8, 0, 0, 0, 1, 0, 9, 3], [9, 4, 0, 6, 0, 3, 0, 0, 0], [0, 6, 0, 9, 0, 0, 8, 0, 0], [0, 0, 5, 0, 0, 4, 0, 3, 9], [0, 5, 4, 8, 0, 2, 0, 0, 0], [1, 9, 6, 0, 0, 0, 0, 0, 8], [0, 2, 7, 0, 0, 9, 4, 5, 0]], [[3, 0, 8, 0, 0, 0, 0, 0, 0], [6, 0, 7, 3, 1, 0, 8, 4, 0], [0, 9, 1, 0, 0, 0, 0, 0, 7], [0, 4, 0, 0, 2, 5, 0, 0, 0], [0, 6, 9, 4, 7, 0, 0, 3, 0], [5, 7, 0, 9, 0, 6, 0, 0, 1], [0, 0, 4, 7, 6, 0, 5, 2, 0], [0, 0, 6, 0, 0, 3, 9, 0, 4], [0, 0, 0, 0, 0, 0, 0, 0, 8]], [[7, 9, 0, 0, 0, 1, 0, 2, 0], [5, 0, 0, 4, 0, 0, 9, 0, 0], [0, 1, 6, 0, 2, 9, 7, 3, 0], [9, 0, 0, 7, 4, 2, 0, 5, 3], [2, 4, 0, 0, 0, 0, 0, 0, 0], [8, 5, 0, 0, 0, 0, 0, 9, 0], [1, 0, 0, 2, 0, 3, 0, 0, 0], [0, 0, 0, 0, 1, 4, 0, 0, 0], [0, 0, 5, 9, 0, 7, 3, 0, 0]]]