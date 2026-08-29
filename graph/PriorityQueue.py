class Node[T]:

    def __init__(self,data:T,node_id,priority):
        self.priority = priority
        self.data:T = data
        self.node_id = node_id

    def get_id(self):

        return self.node_id

    @classmethod
    def create_nodes(cls,array):

        nodes = []

        for i in range(len(array)):

            nodes.append(Node(array[i],node_id=f"node-{i}",priority=-1))

        return nodes


    @classmethod
    def nodes_to_list(cls,nodes):

        nodes_x = [f" node_id =>{node.node_id}  data=>{node.data} ,priority =>{node.priority}" for node in nodes]

        return nodes_x




class PriorityQueue[T]:

    def __init__(self,size):
        self.type ='max'
        self.capacity=size
        self.occupied=0
        self.items = []
        self.pos ={}
        

     

            
        
        
            
    def swap(self,index1,index2):

        self.pos[self.items[index1].node_id] = index2
        self.pos[self.items[index2].node_id] = index1
        self.items[index1],self.items[index2] = self.items[index2],self.items[index1]

    def setType(self,type):

        self.type = type

    def setData(self,data):

        self.items = data

    def parent_index(self,index):

        if index <=0 or index >=self.size:

            return -1

        return (index-1)/2 


    def left_child_index(self,index):
 
        if index <=0 or index >=self.size:

            return -1

        return (2* index)+1


    def right_child_index(self,index):
            

        if index <=0 or index >=self.size:

            return -1

        return (2*index)+2


    def percolate_down(self, index):
        size = len(self.items)
        i = index

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            target = i

            if self.type == "max":
            # Check if left child is larger than current
                if left < size and self.items[left].priority > self.items[target].priority:
                    target = left
            # Check if right child is even larger than current best
                if right < size and self.items[right].priority > self.items[target].priority:
                    target = right
            else:  # min heap
            # Check if left child is smaller than current
                if left < size and self.items[left].priority < self.items[target].priority:
                    target = left
            # Check if right child is even smaller than current best
                if right < size and self.items[right].priority < self.items[target].priority:
                    target = right

        # If the largest/smallest node is already at index i, heap property is restored
            if target == i:
                break

        # Swap and continue down
            self.swap(i, target)
            i= target



    

                
    def percolate_up(self,index):

        i = index

        # parent_index = self.parent_index(i)

        if self.type == 'max':

            while i > 0 and  self.items[(i-1)//2].priority < self.items[i].priority:

                # self.items[(i-1)//2],self.items[i] = (self.items[i],self.items[(i-1)//2] )

                self.swap(i,(i-1)//2)

                i = (i-1)//2

        else:

            while i > 0 and  self.items[(i-1)//2].priority > self.items[i].priority:

                # self.items[(i-1)//2],self.items[i] = (self.items[i],self.items[(i-1)//2] )

                self.swap(i,(i-1)//2)

                i = (i-1)//2



    def enque(self,item:T):

            print(f"equeing {item.data}  into current size {self.capacity} and occupied size {len(self.items)}")

            if self.occupied == self.capacity :

                raise ValueError("SIZE IS FULL")

            self.items.append(item)

            self.pos[item.node_id] = len(self.items)-1
            self.occupied= len(self.items) # updated occupied counter 

            self.percolate_up(len(self.items)-1)



    def deque(self):

        # checks if queue is empty
        if self.occupied ==0:
            raise ValueError("queue is empty")

        # save the root element
        x=self.items[0]

        self.items[0] = self.items[-1]

        self.pos[self.items[0].node_id] = 0 

        #delete position record 
        del self.pos[x.node_id]

        # self.items[0] = self.items[-1]

        del self.items[-1]

        self.occupied  = len(self.items)

        self.percolate_down(0)

        return x 






    

    
    def updatePriority(self,node_id,new_priority):

        if not node_id in self.pos:
            print('node id does not exist')
            return False

        index = self.pos[node_id]

        print(f"updating priority for {node_id} with index {index}") 
        

        old_priority = self.items[index].priority

        self.items[index].priority = new_priority

        if (self.type =='max' and  new_priority > old_priority) or (self.type=='min' and new_priority < old_priority):

            self.percolate_up(index)

        else:
            self.percolate_down(index)




        # milestone 1 : find the node reference by looking it up




        





        
        



        