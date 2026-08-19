from graph.Graph import Graph 


def valid_color(graph,curret_color,color_assignment,vertex):


    for neighbour in graph.adj_list[vertex]:

        if  color_assignment [neighbour] and color_assignment[neighbour] == curret_color:

            return False


    return True


def formatize(arr):
    res = []

    for i,v in arr:
        res.append(f" vertex {i} => color {v}  ")

    return res


def colorize(vertex,graph,color_options,color_assignment,res):



    # base case reached end means all vertex were completed

        if vertex == graph.vertices and color_assignment not in res:
             res.append(color_assignment.copy())
             return

        for color in color_options:

            if valid_color(graph,color,color_assignment,vertex):

                  color_assignment[vertex] = color

                  colorize(vertex+1,graph,color_options,color_assignment,res)

                  color_assignment[vertex]=None





            
        




        

    








            


        


            

    






   



    

            


    



    

    



test_graph = Graph(3)

test_graph.add_edge(0,1)

test_graph.add_edge(1,2)

# test_graph.add_edge(0,2)a

colors =['red','blue','pink']

color_assignment =[0]*test_graph.vertices

combs = []

colorize(0,test_graph,colors,color_assignment,combs)


print(f"total combibations {len(combs)}")


print(combs)


