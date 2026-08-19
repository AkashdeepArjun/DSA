"""
[ . . . .]   
[ . . . .]   
[ . . . .]
[ . . . .]
 """

def check_along_path (grid,row,col,dr,dc):

    size = len(grid[0])

    if row <0 or col <0 or row>=size or col>=size:

        return False  #base case // where recursion will end

    if grid[row][col] == 'Q':

        return True     # if queen is found return

    if check_along_path(grid,row+dr,col+dc,dr,dc):      #search recursively along that direction

        return True


    return False


def queen_exists(grid ,row,col):


    directions =[(-1,-1),(-1,1),(-1,0),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    for dx,dy in directions:

             if check_along_path(grid,row,col,dx,dy):

                  return True

    return False 



def place_queen(grid,row,col):

     if queen_exists(grid,row,col):

          return False

     else:
          grid[row][col] ='Q'

          return True 

def remove_queen(grid,row,col):

    if queen_exists(grid,row,col):

          grid[row][col]='.'    #removal success 

          return True

    else :

        return False   # queen does not exist at that place


def fill_queen(grid,permutations,row=0):

    if row >= len(grid[0]): # rows finished copy the result

        permutations.append([r[:] for r in grid])

        return  

    for c in range(0,len(grid[0])):

        if place_queen(grid,row,c):

            fill_queen(grid,permutations,row+1)

            remove_queen(grid,row,c)
         
    


    
    

         


    
     

     

    
                  
          
          








if __name__ =='__main__':

    grid = [['.' for _ in range(4)] for _ in range(4) ]

    print("grid is ")

    for row in grid :

        print(row)


    perms =[]


    fill_queen(grid,perms,0)

    for combination in perms:

         print(combination)

    
 







    


    


