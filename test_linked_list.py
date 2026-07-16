from linked_lists.LinkedList import LinkedList 


list = LinkedList()

list.append(4)

list.append(5)

list.append(6)

list.prepend(8)

list.append(9)

list.prepend(8)
list.prepend(8)


print(list.print_linked_list())