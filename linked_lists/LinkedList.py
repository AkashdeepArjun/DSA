from utils.Util import Util

class Node[T]:

    def __init__(self,data:T):
        self.data=data
        self.next=None 

    @classmethod
    def create_node(cls,data:T):
        
        return cls(data)
    
 

    


class LinkedList[T]:
    def __init__(self):
        self.head=None 

    def append(self,data):
        
        if not self.head:
            self.head = Node.create_node(data=data)
            self.next=None 
            return


        ptr = self.head

        while ptr.next:
            ptr= ptr.next
        
        ptr.next = Node.create_node(data=data)



    def prepend(self,data):

        if not self.head:
            self.head = Node.create_node(data=data)
            self.next=None 
            return
        else:
            new_node = Node.create_node(data)
            new_node.next = self.head
            self.head = new_node


    def print_linked_list(self):
        res=[]
        ptr= self.head
        while(ptr):
            res.append(Util.get_info(ptr.data))
            ptr=ptr.next

        return res





