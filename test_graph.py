from graph.Graph import Graph


N = int(input("Enter number of vertices: "))

g = Graph(N) 

edges = int(input("Enter number of edges: "))

for i in range(edges):
    src,dest = map(int,input("Enter edge: ").split())
    g.add_edge(src,dest)    


res_dfs = []
g.dfs(0,res_dfs)

g.reset()

res_bfs = []
g.bfs(0,res_bfs) 

print("DFS Traversal: ",res_dfs)
print("BFS Traversal: ",res_bfs)