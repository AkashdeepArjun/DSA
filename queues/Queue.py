
class Queue[T]:
    def __init__(self,size:int):
        self.size=size
        self.entries:list[T] =[None]*self.size 
        self.front= -1
        self.rear =-1

    def enque(self,item:T):
        if self.front==0 and (self.entries.count(None)==0 and len(self.entries)==self.size):
            raise ValueError("QUEUE IS FULL") 
        self.rear+=1
        self.entries[self.rear]= item 
        # self.size+=1

        if self.front == -1:
            self.front=0

    def reset(self):
        self.front = -1
        self.rear =-1 
        self.entries =[None]*self.size

    def peek(self):
        return self.entries[self.front:self.rear+1]

    def deque(self):
        if  self.front == -1 and self.rear == -1:
            raise ValueError("QUEUE is  empty")       
        res= self.entries[self.front]
        # del self.entries [self.front]
        self.front+=1
        # self.size-=1

        if self.front  > self.rear:
            self.reset()

        return res

    def is_empty(self):
        return self.front == -1 and self.rear == -1