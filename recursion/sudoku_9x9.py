
import random

def valid_cell(grid,row,col,target):

    # check entire row and column 

    for i in range(9):
        if grid[i][col] == target: #check rows
            return False
        if grid[row][i] == target: #check cols
            return False



    #check 1 3x3 grid 
    row_start = (row //3)*3
    col_start  = (col // 3)*3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):

            if grid[r][c] == target:
                return False


    return True
    

    





def solve_sudoku(grid,row,col):

    if row == 9:
        return True

    if col == 9:
        return solve_sudoku(grid,row+1,0)

    if grid[row][col]!='.':
        return solve_sudoku(grid,row,col+1)

    for number in range(1,10):

        if valid_cell(grid,row,col,number):

            grid[row][col]=number

            if solve_sudoku(grid,row,col+1):
                return True

            grid[row][col]='.'

            




    return False

    

   



if __name__ =='__main__':

    grid = [['.' for _ in range(9) ] for _ in range(9)]

    print(grid)

    used_nums=[]

    # combs =[]

    solve_sudoku(grid,0,0)

    print(grid) 