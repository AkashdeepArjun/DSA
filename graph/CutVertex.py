from collections import deque
import sys
import os 
sys.path.append(os.path.abspath("../"))

from graph.Graph import Graph


def dfs_cut_vertex(g:Graph,source,visited,parent,low,disc,cut_vertices,nums):

    visited.add(source)
      
    children = 0

    low[source] = disc[source] = nums


    for v in g.adj_list[source]:
        if v not in visited:
            children+=1
            parent[v] = source
            dfs_cut_vertex(g,v,visited,parent,low,disc,cut_vertices,nums+1)

            low[source] = min(low[source],low[v])

            if parent.get(source) is None and children>1:
                cut_vertices.add(source)

            if parent.get(source) is not None and low[v]>=disc[source]:
                cut_vertices.add(source)

        elif v != parent.get(source):
            low[source] = min(low[source],disc[v])

        else:
            continue




def cut_vertex(g:Graph):

    visited=set()
    cut_vertices=set()
    parent={}

    nums = 0

    low = {v: float('inf') for v in range(g.vertices)}
    disc = {v: float('inf') for v in range(g.vertices)}

    for v in range(g.vertices):
        if v not in visited:
            dfs_cut_vertex(g,v,visited,parent,low,disc,cut_vertices,nums)

    return cut_vertices


def test():

    g= Graph(4)

    edges = [(0,1),(0,2),(2,3)]

    for u, v in edges:
        g.add_edge(u, v)

    cut_vertices = cut_vertex(g)
    print("Cut vertices:", cut_vertices)



if __name__ == "__main__":
    test()