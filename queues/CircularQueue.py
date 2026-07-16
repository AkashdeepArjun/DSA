
class CircularQueue[T]:
    
    def __init__(self,size:int):
        self.size=size
        self.enteries:list[T] =[None]* self.size 
        self.front = -1 
        self.rear = -1
        self.filled=0


    def enque(self,item:T):
        if self.front == (self.rear+1)% self.size:
            raise ValueError("QUEUE IS FULL")
        
        self.rear = (self.rear+1)%(self.size)
        print(f"ENQUENING {item} REAR IS {self.rear}")

        self.enteries[self.rear] = item
        self.filled +=1
        if self.front == -1:
            self.front =0



    def deque(self):
        if self.filled ==0 :
            raise ValueError("QUEUE IS EMPTY")
        
        x = self.enteries[self.front]

        self.front = (self.front+1) % (self.size)




        self.filled-=1

        return x
    
    def is_empty(self):
        return self.front == -1 and self.rear == -1 
    
    def peek(self):
        if self.front > self.rear:
            return self.enteries[self.front:self.rear+1]
        elif self.front < self.rear:
            return self.enteries[self.front:self.rear+1:-1]
        return self.enteries[self.front]