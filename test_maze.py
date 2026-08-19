from utils.Util import make_2d_array
from codechef.maze import travel
row,col = map(int,input("enter rows and cols of grid ").split())

grid = make_2d_array(row,col,1)

ix,iy = map(int,input("Enter the initial coordinates (x y): ").split())
tx,ty = map(int,input("Enter the target coordinates (x y): ").split())



num_block_cells = int(input(" number of block cells"))

for i in range(num_block_cells):

    br,bc=map(int,input().split())

    if br >= row or bc >=col:

        raise ValueError("INVALID COORDINATES")

    grid[br][bc] =0


res=[]
visited=make_2d_array(row,col,0)
subset=[]

travel(grid,ix,iy,tx,ty,row,col,visited,subset,res)

print(res)

