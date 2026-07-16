
class Heap[T]:

    def __init__(self):
        self.items = []
        self.size = 0
        self.heap_type = "MAX"  # Default heap type is MAX

    def set_type(self, type: str):
        if type not in ["MAX", "MIN"]:
            raise ValueError("Type must be either 'MAX' or 'MIN'")
        self.heap_type = type

    def set_items(self, items: list[T]):
        self.items = items
        self.size = len(items)
        self.build_heap()
    

    def __init__(self,items: list[T] = None):
        self.items = items if items is not None else []
        self.size = len(self.items)
        self.heap_type = "MAX"  # Default heap type is MAX
        self.build_heap()


    def left_child_index(self, index: int) -> int:
       if index < 0 or index >= self.size:
            return -1
       else:
            return 2 * index + 1
        

    def right_child_index(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            return 2 * index + 2
        

    
    def parent_index(self, index: int) -> int:
       if index <= 0 or index >= self.size:
            return -1
       else:
            return (index - 1) // 2
       

    def percolate_down(self, index: int):
            if self.heap_type == "MAX":
                l = self.left_child_index(index)
                r = self.right_child_index(index)
                
                if l==-1 and r==-1:
                    return
                
                max_index = index

                if l < self.size and self.items[l] >  self.items[index]:
                    max_index = l

                if r < self.size and self.items[r] > self.items[max_index]:
                    max_index = r

                if max_index != index:
                    self.items[index], self.items[max_index] = self.items[max_index], self.items[index]
                    self.percolate_down(max_index)

            else:



                l = self.left_child_index(index)
                r = self.right_child_index(index)
                
                if l==-1 and r==-1:
                    return
                
                min_index = index

                if l < self.size and self.items[l] <  self.items[index]:
                    min_index = l

                if r < self.size and self.items[r] < self.items[min_index]:
                    min_index = r

                if min_index != index:
                    self.items[index], self.items[min_index] = self.items[min_index], self.items[index]
                    self.percolate_down(min_index)



    def percolate_up(self, index: int):
        if self.heap_type == "MAX":
            parent = self.parent_index(index)
            if parent != -1 and self.items[index] > self.items[parent]:
                self.items[index], self.items[parent] = self.items[parent], self.items[index]
                self.percolate_up(parent)
            else:
                return
        else:
            parent = self.parent_index(index)
            if parent != -1 and self.items[index] < self.items[parent]:
                self.items[index], self.items[parent] = self.items[parent], self.items[index]
                self.percolate_up(parent)
            else:
            
                return
        


    def build_heap(self): 
        for x in range(self.size // 2 - 1, -1, -1):
            self.percolate_down(x)


    def heap_sort(self,list: list[T]) -> list[T]:
        self.items = list
        self.size = len(list)
        self.build_heap()
        sorted_list = []
        while self.size > 0:
            sorted_list.append(self.items[0])
            self.items[0] = self.items[self.size - 1]
            self.size -= 1
            self.percolate_down(0)
        return sorted_list

        
    def kth_largest(self, k: int) -> T:
        if self.heap_type != "MAX":
            raise ValueError("Heap type must be MAX to find kth largest")
        if k <= 0 or k > self.size:
            raise ValueError("k must be between 1 and the size of the heap")
        temp_heap = Heap(self.items.copy())
        temp_heap.heap_type = "MAX"
        for _ in range(k - 1):
            temp_heap.items[0] = temp_heap.items[temp_heap.size - 1]
            temp_heap.size -= 1
            temp_heap.percolate_down(0)
        return temp_heap.items[0]

    def kth_smallest(self, k: int) -> T:

        if self.heap_type != "MIN":
            raise ValueError("Heap type must be MIN to find kth smallest")
        if k <= 0 or k > self.size:
            raise ValueError("k must be between 1 and the size of the heap")
        temp_heap = Heap(self.items.copy())
        temp_heap.heap_type = "MIN"
        for _ in range(k - 1):
            temp_heap.items[0] = temp_heap.items[temp_heap.size - 1]
            temp_heap.size -= 1
            temp_heap.percolate_down(0)
        return temp_heap.items[0]
