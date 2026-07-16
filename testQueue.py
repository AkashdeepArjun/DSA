from queues.Queue import Queue 


q = Queue[int](3)
try:
  
 for i in range(4,8):
      q.enque(i)
    # x :int = q.deque()
        

except ValueError as e:

        print(f"error occured {e}")

except Exception as other:
    print(f" other issue {other}") 


finally:
     
     print(q.entries)
     q.deque()
     q.deque()
     q.deque()

     print("final queue",q.entries)