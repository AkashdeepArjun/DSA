from queues.Queue import Queue

class Edge[T]:

    def __init__(self,src:T,dest:T):
        self.src:T=src 
        self.dest:T=dest

    def get_edge(self):
        return {"src":self.src,"dest":self.dest}
    

a = Edge[float](1.0,2.0)
b= Edge[float](3.0,4.0)

q = Queue[Edge](3)
try:
    q.enque(a)
    q.enque(b)

    for i in range(len(q.entries)):
        if q.entries[i]:
            print(q.entries[i].get_edge())


    q.deque()
    q.deque()

    for i in range(len(q.entries)):
        if q.entries[i]:
            print(q.entries[i].get_edge())
    




except Exception as a:
    print(a)