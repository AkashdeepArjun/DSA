



def test():

    list =[(0,1),(0,2),(1,3),(2,3)]

    print(f"original list {list}")

    weights =[ [ 0 for _ in range(4)  ] for _ in range(4) ] 

    weights[0][1] =1 

    weights[0][2] = 4

    weights [2][3] = -1

    weights [1][3] = 2

    d = sorted(list,key=lambda x:weights[x[0]][x[1]])

    print(f"modified list {d}")






if __name__ == '__main__':

    test()






