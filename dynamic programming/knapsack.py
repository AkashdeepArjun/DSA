
# top down approach 
def knapsack(items, index, budget, memo=None):
    if memo is None:
        memo = {}

    # Base case: reached end of items or budget exhausted
    if index == len(items) or budget == 0:
        return 0

    # 1. State must include BOTH index and remaining budget
    state = (index, budget)
    if state in memo:
        return memo[state]

    # Choice 1: SKIP the current item
    skip = knapsack(items, index + 1, budget, memo)

    # Choice 2: PICK the current item (if affordable)
    pick = 0
    if items[index]["price"] <= budget:
        pick = 1 + knapsack(
            items, index + 1, budget - items[index]["price"], memo
        )

    # Store the best outcome for this exact (index, budget) combination
    memo[state] = max(skip, pick)
    return memo[state]


def knapsack_bottm_up(items,budget):                    
                                                                                            # index =1 ,budget =

    n = len(items)

    dp =[[0]* (budget+1) for _ in range(n+1) ]

    for index in range(1,n+1):

        price = items[index-1]["price"]

        for b in range(budget+1):

            dp[index][b] = dp[index-1][b] # previous row 

            if price <=b:

                dp[index][b] = max(dp[index][b], 1+ dp[index-1][b-price] )


    return dp[n][budget]






    


if __name__ =="__main__":


    items =[{"id":124,"price":200} ,{"id":32,"price":342},{"id":43,"price":321},{"id":211,"price":600} ]

    print("items are ")

    for item in items:
        print(item)

    budget = int(input("enter budget please"))

    memo=1

    res = knapsack(items,0,budget)

    print(f" total number of items can be bought is {res}")
             