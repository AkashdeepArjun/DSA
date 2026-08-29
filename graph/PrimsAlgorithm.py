from collections import deque
import sys

import os 

sys.path.append(os.path.abspath("./"))

# algorithm for undirected graph  # goal minimum spanning tree


from graph.Graph import Graph 

from graph.PriorityQueue import Node,PriorityQueue


def primsAlgorithn(g:Graph,source:int,weights):

    # requirement 1 priority queue for picking vertex based on distance travel
    pq= PriorityQueue(g.vertices)

    # final result path will be of format v1 ->v2

    path=["" for _ in range(g.vertices)]

    pq.type='min'

    pq.enque(Node(source,node_id=f"v-{source}",priority=-1))

    #distance initalized to every vertex as -1
    dp = [-1] * g.vertices

    # track of visited nodes 
    visited = []

    #distance upto source is  0
    dp[source] = 0

    #iniitalize path from "source"

    path[source] = f"{source}"

    while pq.items:

        x = pq.deque() # pick vertex with minimum distance
        
        visited.append(x.data)

        for w in g.adj_list[x.data]:
            new_distance=weights[x.data][w]
            if w not in visited:

                if dp[w] == -1:

                    dp[w]=new_distance

                    pq.enque(Node(data=w,node_id=f"v-{w}",priority=dp[w]))

                    path[w]=f"{x.data}->{w}"

                elif dp[w] >new_distance:

                    dp[w]=new_distance

                    pq.updatePriority(f"v-{w}",new_distance)

                    path[w]=f"{x.data}->{w}"

                else:
                    continue

    return [path,visited]

def test():

    g = Graph(4)
    g.type='u'

    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(2,3)
    g.add_edge(1,3)


    weights = [[0 for _ in range(g.vertices)] for _ in range(g.vertices)]

    weights[0][1] =1
    weights[0][2] =1
    weights[2][3] =-5
    weights[1][3] = 1


    [path,visited] = primsAlgorithn(g,0,weights)

    for p in path:

        print(p)


    for v in visited:
        print(f"{v}->",end="")



if __name__ == "__main__":

    test()








    




