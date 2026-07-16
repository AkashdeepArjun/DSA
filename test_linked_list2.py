from linked_lists.LinkedList import LinkedList ,Node

class Post:
    def __init__(self ,id,author):
        self.id=id
        self.author =author

    
authors =["akash","aman","vasu"]

posts = []

for i in range(3):
    posts.append(Post(i,authors[i]))


list = LinkedList[Post]()

list.append(posts[0])
list.append(posts[1])
list.prepend(posts[2])

print(list.print_linked_list())







    