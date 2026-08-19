import random

# fill 3x3 grid in way that each cell have unique value and value is between 1 nad 9

def fill(grid,row,col,used_nums):

    # boundries 

    if row > 2 or col >2:
        return


    x = random.randint(1,9)  # pick a random number from 1 to 9

    # if cell is filled
    if grid[row][col] !='.' :

        fill(grid,row,col+1,used_nums)

        fill(grid,row+1,col,used_nums)  

        return 

    # cell is empty     

    if not x in used_nums:

        grid[row][col] = x

        used_nums.append(x)

        fill(grid,row,col+1,used_nums)

        fill(grid,row+1,col,used_nums)

    else:

        fill(grid,row,col,used_nums)


if __name__ =='__main__':

    grid = [['.' for _ in range(3) ] for _ in range(3)]

    print(grid)

    used_nums=[]

    # combs =[]

    fill(grid,0,0,used_nums)

    print(grid)  


    