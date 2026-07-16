class Stack[T]:
    def __init__(self,size:int):
        
        self.size=size
        self.items:list[T]=[0]*self.size
        self.top=-1


    def push(self,item:T):
        print(f"pushing ..{item}")
        if self.top ==self.size-1:
            raise ValueError("OVERFLOW")
        self.top = self.top + 1
        # print("top is ",self.top)
        self.items[self.top] = item
        self.size=len(self.items)

    def pop(self):
        if self.top ==-1:
            raise ValueError("UNDERFLOW")
        res =self.items[self.top]
        self.items[self.top:self.top+1] = []
        self.size-=1
        self.top-=1
        return res
    
    


    # def print_stack(self):

    #     res =[]
    #     for i in range(self.size):
    #         res.append(self.items[i])

    #     return res