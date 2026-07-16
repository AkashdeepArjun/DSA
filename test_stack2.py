from stack.Stack import Stack

class Edge[T]:

    def __init__(self,src:T,dest:T):
        self.src:T=src 
        self.dest:T=dest

    def get_edge(self):
        return {"src":self.src,"dest":self.dest}
    

a = Edge[float](1.0,2.0)
b= Edge[float](3.0,2.0)

stack = Stack[Edge](3)

stack.push(a)
stack.push(b)

for top in range(stack.top+1):
    print(stack.items[top].get_edge())
