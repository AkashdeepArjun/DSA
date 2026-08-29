

# each ladder can be either steps in one or two 


def climb(curr_height,ladder_height,options_picked,res ):

    if curr_height == ladder_height:                                
        res.append(options_picked.copy())                          
        return  

    if curr_height > ladder_height:
        return                                            

    for jump in range(1,3):

        options_picked.append(jump)

        climb(curr_height+jump,ladder_height,options_picked,res)

        options_picked.pop()



if __name__ == '__main__':

    h=3
    res=[]
    options=[]

    climb(0,h,options,res)

    print(res)


    
