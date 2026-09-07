
import sys
import os 
sys.path.append(os.path.abspath("../"))




def check_along_path (grid,row,col,dr,dc,index,word):

    size = len(grid[0])

    if row <0 or col <0 or row>=size or col>=size:

        return False  #base case // where recursion will end

    if grid[row][col] == word[index]:

        return True     # if queen is found return

    if check_along_path(grid,row+dr,col+dc,dr,dc):      #search recursively along that direction

        return True


    return False



def make_grid(size):

    grid = [['.' for _ in range(size)] for _ in range(size)]

    return grid

def add_letter(grid,row,col,letter):

    size = len(grid[0])
    assert row >=0 and row <=size 

    assert col >=0 and col <=size

    grid[row][col] = chr(letter)


def print_grid(grid):

    for row in grid:
        print(row)




def word_search(grid,row,col,index,word,visited,records):

    # boundries if rows are done means no search was found 

    if row <0 or row >=len(grid):
        return False
    # if columns are done means no search was found
    if col <0 or col >=len(grid):
        if index ==0:# if we are at the first index of the word and we have reached the end of the column, we can move to the next row
            return word_search(grid,row+1,0,index,word,visited,records)
        return False # if we are not at the first index of the word and we have reached the end of the column, we cannot move to the next row, so we return False

    # if the current cell is already visited, we cannot use it again
    if visited[row][col]:
        return False

    if index == len(word): # if we have found the entire word, we return True
        return True

    directions = [(0,1),(1,0),(0,-1),(-1,0)] # right, down, left, up

    for dr, dc in directions:
        if check_along_path(grid,row,col,dr,dc,index,word):
            visited[row][col] = True
            records.append((row,col))
            if word_search(grid,row+dr,col+dc,index+1,word,visited,records):
                return True
            visited[row][col] = False
            records.pop()
    

    


if __name__ == "__main__":
    
    size = 5
    grid = make_grid(size)
    add_letter(grid,0,0,ord('H'))
    add_letter(grid,0,1,ord('E'))
    add_letter(grid,0,2,ord('L'))
    add_letter(grid,0,3,ord('L'))
    add_letter(grid,0,4,ord('O'))

    visited = [[False for _ in range(size)] for _ in range(size)]
    records = []
    word = "HELLO"
    if word_search(grid,0,0,0,word,visited,records):
        print(f"Word '{word}' found at positions: {records}")
    else:
        print(f"Word '{word}' not found.")