from graph.Graph import Graph



vertices = int(input("enter number of vertices"))

edges = int(input("enter number of edges")) 

# v* v-1 is for undirected and v * (v-1) /2 

limit = vertices * (vertices //2)

if edges > limit :

    print(f"edges can not be more than {limit}")

    exit


g = Graph(vertices)

g.type ='d'

for e in range(edges):

    x1,x2 = map(int,input("add  src and dest for edge").split())

    g.add_edge(x1,x2)


print("graph is ")

g.print_graph()

res = g.topological_sort()

print(f" ordering is {res}")
