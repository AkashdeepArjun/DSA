from queues.Queue import Queue 

my_queue = Queue[int](3)

try:

    for i in range(4,7):
        print(f"ENQUEING {i}....")
        my_queue.enque(i)
        print(f"items left {my_queue.entries} FRONT : {my_queue.front} REAR:{my_queue.rear} SIZE:{my_queue.size}")

        

    # for j in range(5):
    #     my_queue.enque(j)

    #     print("TEST OVER FLOW ",my_queue.entries)


    for i in range(3):
        x = my_queue.deque()
        print(f"DEQUEUED {x} ITEMS LEFT {my_queue.entries} FRONT: {my_queue.front} REAR :{ my_queue.rear} SIZE:{my_queue.size}  ")

    my_queue.deque()
    print("TEST DEQUE QUE IS ")


except Exception as e:
    print(f"Excepetion occured",e)

finally:


    print(" FINALL BLOCK :que are ",my_queue.entries)
