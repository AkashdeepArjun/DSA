class DisjointSet:

    def __init__(self,size):
        self.size = size
        self.parent= [-1 ]*self.size
        self.ranks = [ -1 ]*self.size


    def find(self,x):

        if not x>=0 and not x<self.size:
                
            return -1

        elif self.parent[x] < 0:
            return x
            
        else:
            return self.find(self.parent[x])


    def union(self,x1,x2):

        root1= self.find(x1)

        root2 = self.find(x2)

        if root1 == root2 and root1!=-1:
        
            return 

        elif self.ranks[root2]<self.ranks[root1]:
            
            self.ranks[root2]-=1
            
            self.parent[root1]=root2
    
            print(f"parent of {root1} is set to {root2}")
        else:
            self.ranks[root1]-=1

            self.parent[root2]=root1


            print(f"parent of {root2} is set to {root1}")



    def tree(self,x,path):

        if not x>=0 and not x<self.size:
                
            return -1

        path.append(x)

        if self.parent[x] < 0:
            path.append(x)
            return x
            
        else:
            return self.find(self.parent[x])



def test():

    ds = DisjointSet(3)

    ds.union(0,1)

    ds.union(1,2)
    
    print(ds.parent)




if __name__ =='__main__':

    test()
        
        
