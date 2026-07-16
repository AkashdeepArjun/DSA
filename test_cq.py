from queues.CircularQueue import CircularQueue 


test_queue = CircularQueue[int](3)


for i in range(1,4):
    print(f"ENQUEING .... {i}   ")
    test_queue.enque(i)
    print(f"CURRENT QUEUE { test_queue.peek()} FRONT :{test_queue.front} REAR:{test_queue.rear} FILLED {test_queue.filled}")


print (" testin dequeue ")

x= test_queue.deque()
print(f" DEQUED {x} CURRENT QUEUE { test_queue.peek()} FRONT :{test_queue.front} REAR:{test_queue.rear} FILLED {test_queue.filled}")

test_queue.enque(4)
print(f"CURRENT QUEUE { test_queue.enteries} FRONT :{test_queue.front} REAR:{test_queue.rear} FILLED {test_queue.filled}")

    
# for i in range(1,4):
   
#     x =test_queue.deque()
#     print(f" DEQUED { x} CURRENT QUEUE { test_queue.enteries} FRONT :{test_queue.front} REAR:{test_queue.rear} FILLED {test_queue.filled}")


# test_queue.deque()