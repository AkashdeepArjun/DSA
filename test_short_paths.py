from graph.Graph import Graph



v = int(input("enter number of vertices"))

e = int(input("enter number of edges"))

limit = v * (v-1)


assert e <= limit  

g = Graph(v)

for i in range(e):

    src,dest = map(int,input("enter source and destination ").split())

    g.add_edge(src,dest)

res = g.short_paths(0)

print("final result is ")

print(res)

    
