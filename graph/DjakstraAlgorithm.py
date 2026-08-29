
from PriorityQueue import Node,PriorityQueue
from Graph import Graph

# can handle only positive edges 
def djakstra(g:Graph,graph_weights,source):

    distance = [-1 for _ in range(g.vertices)]

    path=["" for _ in range(g.vertices)]

    pq= PriorityQueue(5)

    pq.setType('min')

    # step 1 : enqueue element
    pq.enque(Node(source,node_id=f"v-{source}",priority=-15))
    distance[source] = 0
    path[source] = f"{source}"
    while pq.items:

       x = pq.deque()

       for neighbour in g.adj_list[x.data]:

        print(f"target {x.data} neighbour:{neighbour}")

        cd= distance[x.data]+graph_weights[x.data][neighbour]

        if distance[neighbour] == -1 :

           distance[neighbour] = cd 

           path[neighbour] = f"{path[x.data]}  ->{neighbour}"

           pq.enque(Node(neighbour,f"v-{neighbour}",priority=cd))

           print(f"node with vertex {neighbour} was saved in index {pq.pos[f"v-{neighbour}"]} and vertex is {pq.items[pq.pos[f"v-{neighbour}"]].data}     ")


        if distance[neighbour] > cd :

            
            distance[neighbour] = cd    
            # path[x.data].append(f"{x.data} => {neighbour} current_distance:{graph_weights[x.data][neighbour]} total distance:{distance[neighbour]}")
            # path[neighbour] = x.data

            path[neighbour] = f"{path[x.data]}  ->{neighbour}"
            
            pq.updatePriority(f"v-{neighbour}",new_priority=cd)
            


    return path
    








  
def test():

    g = Graph(5)
    g.type='d'
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(2,1)
    g.add_edge(2,3)
    g.add_edge(1,4)
    g.add_edge(3,4)


    g.print_graph()


    weights = [[ 0 for _ in range(g.vertices) ] for _ in range(g.vertices)]

    weights[0][1] = 4
    weights[0][2] = 1
    weights[2][1] = 2
    weights[2][3] = 4
    weights[1][4] = 4
    weights[3][4] = 4


    path = djakstra(g,weights,0)

    print(path)

    #  for i in range(g.vertices):
    #     print(f"distance[{i}] = {distance[i]}")



if __name__ =='__main__':

      test()








     

