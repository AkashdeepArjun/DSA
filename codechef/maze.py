

def travel(grid,row,col,tr,tc,max_rows,max_cols,visited,subset,result):

        if row <0 or row >=max_rows or  col <0 or col >=max_cols:
             return

        if grid[row][col]==0:
            return 
        
        if visited[row][col]:
             return

        if row == tr and col == tc:
             result.append("".join(subset))
             return

        visited[row][col]=1

        directions =[ ("L",0,-1),("R",0,1),("U",-1,0),("D",1,0)]

        for dir,row_offset,col_offet in directions:

             subset.append(dir)
             travel(grid,row+row_offset,col+col_offet,tr,tc,max_rows,max_cols,visited,subset,result)
             subset.pop()


        visited[row][col]=0



        


        







