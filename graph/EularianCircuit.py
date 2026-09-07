from collections import deque
import sys
import os 
sys.path.append(os.path.abspath("../"))

from graph.Graph import Graph


def degree(g:Graph,node):

    
    incident_edges=0

    for v in range(g.vertices):
        if node in g.adj_list[v]:
            incident_edges+=1

    return incident_edges


def every_vertex_even(g:Graph):
    count=0
    for v in range(g.vertices):

        if degree(g,v)%2==0:
            count+=1

    return count == g.vertices


def exactly_two_vertex_odd(g:Graph):

    count=0
    odd_vertices=[]

    for v in range(g.vertices):
        if degree(g,v)%2 !=0:
            odd_vertices.append(v)
            count+=1
            

    return count ==2,odd_vertices


        


# goal : whever any euralian path exists return one of those
def dfs_eularian_undirected(graph:Graph,node,path,used_edges,max_edges,res):

    if len(used_edges) == max_edges:
        res.append(path.copy())
        # print(f"final result is {res}")
        return True

    # path.append(node)
    if node not in path:
        path.append(node)

    for neighbour in graph.adj_list[node]:
        # edge 1,2 and 2,1 will be treaed as same
        edge = tuple(sorted([node,neighbour]))

        if edge not in used_edges:
            used_edges.add(edge)
            # print(f"current used edges {used_edges}")
            path.append(neighbour)
            # print(f"current path :{path}")
            if dfs_eularian_undirected(graph,neighbour,path,used_edges,max_edges,res):
                return True
            else:
                used_edges.remove(edge)
                path.pop()


    return False


def dfs_eularian_paths(g:Graph,node,path,used_edges,max_edges,options):

    if len(used_edges) == max_edges:
        options.append(path.copy())
        return

    if node not in path:
        path.append(node)

    for neighbour in g.adj_list[node]:

        edge = tuple(sorted([node,neighbour]))

        if edge not in used_edges:
            #include
            used_edges.add(edge)

            path.append(neighbour)

            #explore
            dfs_eularian_paths(g,neighbour,path,used_edges,max_edges,options)

            #exclude

            used_edges.remove(edge)
            path.pop()






    
def test():

    g=Graph(5)

    edges=[(0,2),(0,1),(1,4),(1,3),(2,3),(3,4)]

    for src,dest in edges:
        g.add_edge(src,dest)

    used_edges=set()

    res=[]

    path=[]

    #all vertices even
    case_a= every_vertex_even(g)

    # exactly 2 odd degree vertices
    case_b,vertices=exactly_two_vertex_odd(g)

    print(f"vertices are {vertices}")


    if case_a:
        # print("first case is occured")
        # dfs_eularian_undirected(g,0,path,used_edges,6,res)

        dfs_eularian_paths(g,0,path,used_edges,len(edges),res)

        for circuit in res:
            print(f"circuit is {circuit}")

    elif case_b:

        for v in vertices:

            print(f"processing {v}")

            # dfs_eularian_undirected(g,v,path,used_edges,6,res)
            
            dfs_eularian_paths(g,v,path,used_edges,len(edges),res)

            for p in res:
                print(f"paths options is {p}")

            path=[]

            used_edges =set()

            res=[]





    else:
        print(f" no eular path/circuit exist")






if __name__ =="__main__":

    test()



           

    




        

        






    



