
from collections import deque
import sys
import os 
sys.path.append(os.path.abspath("../"))


from graph.Graph import Graph

from disjoint_sets.DisJointSet import DisjointSet

def kruskalAlgorithm(g:Graph,edges,weights):

    res=[]

    ds = DisjointSet(g.vertices)
    edges = sorted(edges,key=lambda x:weights[x[0]][x[1]])

    print(f"input edges are {edges}")
    for u,v in edges:
        if ds.find(u) != ds.find(v):
            res.append((u,v))
            ds.union(u,v)

    return res 



def test():

    g= Graph(4)
    
    edges = [(0,1),(0,2),(2,3),(1,3)]


    for u,v in edges:
        g.add_edge(u,v)

    weights =[ [ 0 for _ in range(4) ] for _ in range(4)]


    weights[0][1] =1

    weights[0][2] = 4

    weights[1][3] =2

    weights[2][3] = 3


    min_tree = kruskalAlgorithm(g,edges,weights)


    print(f"result spaanig tree is {min_tree}")




if __name__ =="__main__":
    test()



