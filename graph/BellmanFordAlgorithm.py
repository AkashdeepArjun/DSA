from collections import deque
import sys

import os 


sys.path.append(os.path.abspath("../queues"))



from queues.Queue import Queue 

from graph.Graph import Graph

import math



def bellmanFordAlgorithm(g:Graph,source:int,distance_chart):

    q = deque()

    q.append(source)

    # print(f"queue items are {q.entries}")
    
    path=["" for _ in range(g.vertices)]

    path[source] = f"{source}"

    visited = [0 for _ in range(g.vertices)]

    dp = [math.inf for _ in range(g.vertices)]

    dp[source]=0



    while q:
        x = q.popleft()

        visited[x]=1

        for neighbour in g.adj_list[x]:

                new_distance = dp[x]+distance_chart[x][neighbour]

                if dp[neighbour] > new_distance:

                     dp[neighbour] = new_distance

                     path[neighbour]=f"{x}->{neighbour}"

                     if not visited[neighbour]:
                          q.append(neighbour)

    return path




def testAlgo():

    g= Graph(5)

    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,0)


    weights = [ [ 0 for _ in range(g.vertices)] for _ in range(g.vertices)]

    weights[0][1] = 4
    weights[1][2] = 1
    weights[2][0] = 2

    paths = bellmanFordAlgorithm(g,0,weights)
    
    print(paths)




if __name__ =="__main__":

     testAlgo()
                              


