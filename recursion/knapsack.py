
 #GIVEN ITEMS WE HAVE  to get max number of items we can get under that budget

def knapsack(items, index, budget, options, result):
    # Base Case: processed all items or ran out of budget
    if index == len(items) or budget == 0:
        result.append(options.copy())
        return

    # Choice 1: SKIP the current item
    knapsack(items, index + 1, budget, options, result)

    # Choice 2: PICK the current item (only if affordable)
    current_item = items[index]
    if current_item["price"] <= budget:
        options.append(current_item)  # Choose
        knapsack(
            items, index + 1, budget - current_item["price"], options, result
        )  # Explore
        options.pop()  # Un-choose (Backtrack)

    

    





if __name__ == '__main__':

    items =[{"id":124,"price":200} ,{"id":32,"price":342},{"id":43,"price":321},{"id":211,"price":600} ]

    print("items  are ")

    for item in items:
        print(items)


    capacity = int(input("enter capacity"))

    options = []

    result =[]

    knapsack(items,0,capacity,options,result)

    print("possible result are ")

    for r in result:
        print(r)

        
    
