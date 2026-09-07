from collections import deque
import sys
import os 
sys.path.append(os.path.abspath("../"))

from graph.Graph import  Graph


def dfs_bridge(g:Graph,source,visited,parent,low,disc,bridges,nums):

    visited.add(source)
      
    children = 0

    low[source] = disc[source] = nums


    for v in g.adj_list[source]:
        if v not in visited:
            children+=1
            parent[v] = source
            dfs_bridge(g,v,visited,parent,low,disc,bridges,nums+1)

            low[source] = min(low[source],low[v])

            if low[v]>disc[source]:
                bridges.append((source,v))

        elif v != parent.get(source):
            low[source] = min(low[source],disc[v])

        else:
            continue


def count_bridges(g:Graph):

    visited=set()
    bridges=[]
    parent={}

    nums = 0

    low = {v: float('inf') for v in range(g.vertices)}
    disc = {v: float('inf') for v in range(g.vertices)}

    for v in range(g.vertices):
        if v not in visited:
            dfs_bridge(g,v,visited,parent,low,disc,bridges,nums)

    return bridges


def test():
    g= Graph(3)

    g.type='u'
    
    # edges = [(0,1),(1,2),(1,3),(3,4),(3,5)]

    edges=[(0,1),(1,2),(2,0)]


    for u,v in edges:
        g.add_edge(u,v)

    bridges = count_bridges(g)

    print(f"bridges are {bridges}")


if __name__ =="__main__":
    test()