
# TOP DOWN APPROACH  GOOD FOR DECISON TREE TAKE IT OR LEAVE IT 
def climb_top_down(height:int,cache:dict=None):

    if not cache:
        cache={}

    if height <=2:
        return height


    if height in cache:
        return cache[height]


    cache[height] = climb_top_down(height-1,cache) + climb_top_down(height-2,cache)

    return cache[height]


    # BOTTOM UP APPROACH  TO AVOID RECURSION LIMITS


def climb_bottom_up(height:int):

    dp = [0] *(height+1)

    dp[0]=0

    dp[1]=1

    dp[2] =2

    for h in range(3,height+1):

        dp[h] = dp[h-1]+dp[h-2]

    return dp[height]


if __name__ =='__main__':

    height = int(input("enter height of ladder "))

    print("1. top down approach recursion with memo","2.bottom up approach iterative simply store the results",sep="\n")

    choice = int(input("enter choice "))

    if choice <1 or choice >2 :
        raise ValueError("please enter valid choice only 1 or 2 allowd")

    if choice ==1:

        print(climb_top_down(height=height))

    else:

        print(climb_bottom_up(height))


    






    

    
    