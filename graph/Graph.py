
from collections import deque


class Graph:

    def __init__(self,vertices:int):
        self.type='u'
        self.visted=[False for i in range(vertices)]
        self.adj_list= [[] for i in range(vertices)]
        self.vertices=vertices
        # self.undirected=True


    def add_edge(self,src:int,dest:int):
        if src>=self.vertices or dest>=self.vertices:
            raise Exception(f"Invalid Edge :{src>=self.vertices} or {dest >=self.vertices}")

        if not self.adj_list[src]:
            self.adj_list[src] = []
        
        if self.type == 'u':

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

        
        
        if self.type == 'u':
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

    def indegree(self,target):

        indeg=0

        for v in range(self.vertices):

            if target in self.adj_list[v]:

                indeg+=1

        return indeg 


    def topological_sort(self):

        if self.type =='u':

            print("ordering makes sense for directed graph only bye")

            return 
        
        ordering =[]

        
        queue = deque()

        info_indegree=[0 for _ in range(self.vertices)]

        for v in  range(self.vertices):  # calculate indegree of each first

            info_indegree[v] = self.indegree(v)

            if info_indegree[v] == 0:   #  vertex with 0 indegree will be in queue 

                queue.append(v)

        print(f"indegree of vertices is ",info_indegree)


        while(queue): #process the items with 0 indegree

                x= queue.popleft()

                ordering.append(x)

                for v in range(self.vertices):  # from item to all vertex having edge process and remove edge

                    if v in self.adj_list[x]:
                        print(f" from {x} to {v} we have {self.adj_list[x]}")
                        self.adj_list[x].remove(v)

                        info_indegree[v]-=1

                        if info_indegree[v] ==0:

                            queue.append(v)

        return ordering 



            



        # for all vertices to have edge ends on 

    # equal weighted edge
    def short_paths(self,src):

        dp = [-1] * self.vertices

        q= deque()

        q.append(src)

        dp[src] = 0


        while q:

            source = q.popleft()
            
            for neighbour in self.adj_list[source]:

                if dp[neighbour] == -1:

                    dp[neighbour] = dp[source]+1

                    q.append(neighbour)  


        dp =[ f"{src} can be coverd in {dp[src]} steps" for src in range(self.vertices) ]

        return dp 





