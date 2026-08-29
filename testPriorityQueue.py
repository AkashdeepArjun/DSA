from graph.PriorityQueue import Node ,PriorityQueue 


def test():

 
    # nodes = Node.nodes_to_list(nodes)

    # print(nodes)


    size = int(input(f"enter the size of  queue "))

    data_array = []

    while (len(data_array)<size):

        new_data = int(input("enter new data"))
        data_array.append(new_data)

    
    # data_array = list(map(int,input('add array data').split()))

    
    pq = PriorityQueue(size)

    nodes =Node.create_nodes(data_array)

    type = int(input(f" typeo of queue ? press 1 for max 2 for min default:max"))

    if type ==1:
        pq.type ='max'
    else:
        pq.type ='min'

    

    for i in range(pq.capacity):

        print(f"entering priority for {nodes[i].data} current occupied size is {len(pq.items)}")

        priority = int(input(f" enter priority for {nodes[i].data} "))

        nodes[i].priority = priority

        pq.enque(nodes[i])


    result1 = Node.nodes_to_list(pq.items)
        

    for res in result1:
        print(res)   

    # x = pq.deque()

    print("enter id of given node to update priority")

    for node in pq.items:
        print(node.node_id)

    id = input('enter target_id ')

    new_priority = int(input('priority new'))

    pq.updatePriority(id,new_priority)


    result2 = Node.nodes_to_list(pq.items)
        

    for r in result2:
        print(r)  
        

if __name__ == '__main__':

    test()











