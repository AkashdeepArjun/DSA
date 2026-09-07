from collections import deque
import sys
import os 
sys.path.append(os.path.abspath("../"))

from graph.Graph import Graph


def indeg(g:Graph,node):

    count =0 

    for v in range(g.vertices):

        if node in g.adj_list[v]:
            count+=1

    return count


def outdeg(g:Graph,node):

    c =0 

    for v in range(g.vertices):
        if v in g.adj_list[node]:
            c+=1

    return c









def totalEdges(g:Graph):

    s=0
    for node in g.adj_list:
        s+=len(node)

    return s


def dfs_iterative(g:Graph,node):

    visited= [False for _ in range(g.vertices)]

    stack =[node]

    visited[node]=True

    while stack:

        x = stack.pop()

        for neighbour in g.adj_list[x]:

            if g.adj_list[x][neighbour] and not visited[neighbour]:
                    visited[neighbour] = True

                    stack.append(neighbour)

    return visited


def traspose(g:Graph):

    gt= Graph(g.vertices)

    for u in g.vertices:

        for v in g.vertices:

            if v in  g.adj_list[u]:

                gt.adj_list[v].append(u)

    return gt

def  strongly_connected(g:Graph):

    if g.vertices==0:
        return True

    visited = dfs_iterative(g,0)

    if not all(visited):

        return False


    gt = traspose(g)

    visited_gt = dfs_iterative(g,0)

    if not all(visited_gt):

        return False


    return True




def graphHaveCircuit(g:Graph):

    # edges = totalEdges(g)
    for v in range(g.vertices):

        if indeg(g,v)!=outdeg(g,v):

            return False


    if not strongly_connected(g):

        return False


    return True
   

    

    # return False


def drawEularianCircuit(g:Graph,node,path,used_edges,max_edges,result):

    # success state 
    if len(used_edges) == max_edges:


        result.append(path.copy())

        print(f"final result is {path.copy()}")

        return True

        

    if not node in path:
        path.append(node)

    for neighbour in g.adj_list[node]:

        edge = tuple([node,neighbour])

        if  not edge in used_edges:

            used_edges.add(edge)
            
            print(f"used edge so far {used_edges}")

            path.append(neighbour)

            print(f"path so far {path}")

            if drawEularianCircuit(g,neighbour,path,used_edges,max_edges,result):

                return True

            else:

                used_edges.remove(edge)

                path.pop()


    return False


def explore_eularian(g:Graph,node,path,used_edges,max_edges,eularian_options):

    if len(used_edges) == max_edges:

        eularian_options.append(path.copy())

        return


    if not node in path:
        path.append(node)


    for neighbour in g.adj_list[node]:

        edge = tuple([node,neighbour])

        if not edge in used_edges:

                #include the option
            used_edges.add(edge)

            path.append(neighbour)


                # explore with that option

            explore_eularian(g,neighbour,path,used_edges,max_edges,eularian_options)


                # exclude that option and next iteration will explore  furthur without remembering this

            used_edges.remove(edge)

            path.pop()









    







def test():

    g = Graph(4)

    g.type='d'

    # edges = [(0,1),(1,0),(0,3),(3,0),(2,3),(3,2),(1,2),(2,0),(3,1)]

    edges=[(0,1),(1,0),(0,3),(3,0),(3,2),(2,3),(1,2),(3,1),(2,0)]

    for src,dest in edges:

        g.add_edge(src,dest)


    for v in range(g.vertices):

        inx= indeg(g,v)
        outx = outdeg(g,v)
        print(f" indeg({v}):{inx},outdegree({v}):{outx} matches {inx==outx} ")



    res=[]
    path=[]
    used_edges=set()

    start_point = int(input(f"enter start vertex between 0 and {g.vertices}(exclusive)"))

    assert 0<=start_point <g.vertices

    # drawEularianCircuit(g,start_point,path,used_edges,len(edges),res)

    explore_eularian(g,start_point,path,used_edges,len(edges),res) 
    for option in res:

        print(f"path is {option}")








    # res=[]
    
    # path=[]

    # used_edges=set()

    # drawEularianCircuit(g,0,path,used_edges,len(edges),res)

    # print(f"path is {res} ")





    # graphHaveCycle(g)




if __name__ == "__main__":

    test()



    



