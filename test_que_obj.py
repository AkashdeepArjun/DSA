from queues.Queue import Queue

class User:
    def __init__(self,name,age):
        self.age= age 
        self.name = name 

    def get_info(self):
        return {"user_name":self.name,"user_age":self.age}
    

q = Queue[User](3)

users = [User("akash",32), User("aman",32),User("vasu",30)] 


for user in users:
    print(f"ENUEUING .. {user.name}")
    q.enque(user.get_info())
    print(f"CURRENT QUEUE {q.entries} FRONT {q.front} REAR {q.rear}")

q.enque(users[0])

print("checking dequeu")

for i in range(3):
    x = q.deque()
    print(f" DEQUEUED {x["user_name"]} CURRENT QUEUE {q.entries} FRONT {q.front} REAR {q.rear}")

# q.deque()
