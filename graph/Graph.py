
class Graph:

    def __init__(self,vertices:int):
        self.visted=[False for i in range(vertices)]
        self.adj_list= [[] for i in range(vertices)]
        self.vertices=vertices
        self.undirected=True


    def add_edge(self,src:int,dest:int):
        if src>=self.vertices or dest>=self.vertices:
            raise Exception(f"Invalid Edge :{src>=self.vertices} or {dest >=self.vertices}")

        if not self.adj_list[src]:
            self.adj_list[src] = []
        
        if self.undirected:

            if not self.adj_list[dest]:
                self.adj_list[dest] = []
           
            
            self.adj_list[src].append(dest)
            self.adj_list[src].sort(key=lambda x: x)
            
            self.adj_list[dest].append(src)
            self.adj_list[dest].sort(key=lambda x: x)

        else:
            self.adj_list[src].append(dest)
            self.adj_list[src].sort(key=lambda x: x)


    def remove_edge(self,src:int,dest:int):
        if src>=self.vertices or dest>=self.vertices:
            raise Exception("Invalid Edge")

        
        
        if self.undirected:
            self.adj_list[src].remove(dest)
            self.adj_list[src].sort(key=lambda x: x)


            self.adj_list[dest].remove(src)

            self.adj_list[dest].sort(key=lambda x: x)

        else:
            self.adj_list[src].remove(dest)

            self.adj_list[src].sort(key=lambda x: x)

    def dfs(self,src:int,res):
        if src>=self.vertices:
            raise Exception("Invalid Source")
        
        self.visted[src]=True
        res.append(src)

        for i in self.adj_list[src]:
            if not self.visted[i]:
                self.dfs(i,res)


    def bfs(self,src:int,res):

        if src>=self.vertices:
            raise Exception("Invalid Source")
        
        queue=[]
        queue.append(src)
        self.visted[src]=True

        while queue:
            src=queue.pop(0)
            res.append(src)

            for i in self.adj_list[src]:
                if not self.visted[i]:
                    queue.append(i)
                    self.visted[i]=True

        

    def reset(self):
        self.visted=[False for i in range(self.vertices)]
        # self.adj_list=[[] for i in range(self.vertices)]

    def print_graph(self):
        for i in range(self.vertices):
            print(i,"->",self.adj_list[i])


    def disconnected_components(self):
        components=[]
        for i in range(self.vertices):
            if not self.visted[i]:
                res=[]
                self.dfs(i,res)
                components.append(res)
        
        return components







