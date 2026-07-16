from collections import deque
def max_sum_window(data:list[int], window_size:int) -> int:
        if not data or window_size <= 0:
            return 0
        
        max_sum = 0
        current_sum = sum(data[:window_size])
        max_sum = current_sum   
        for i in range(window_size, len(data)):
            current_sum += data[i] - data[i - window_size]
            max_sum = max(max_sum, current_sum)
        return max_sum 




def max_consecutive(data:list[int],k:int):
    res =[]

    if not data or k ==0:
        return res
    
    deq = deque()

    for index in range(len(data)):
        if deq and deq[0] < (index-k+1):
            deq.popleft()

        while (deq and data[deq[-1]] < data[index]):
            deq.pop()

            
        deq.append(index)

        if index >= k-1:
        
            res.append(data[deq[0]])
             
        
    return res       



def max_consecutiveB(data:list[int],k:int):
    res =[]

    if not data or k ==0:
        return res
    
    deq = deque()

    for index in range(0,len(data),k):
        if deq and deq[0] < (index-k+1):
            deq.popleft()

        while (deq and data[deq[-1]] < data[index]):
            deq.pop()


        deq.append(index)

        if index >= k-1:
        
            res.append(data[deq[0]])
             
        
    return res       
