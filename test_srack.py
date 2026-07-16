from stack.Stack import Stack


stack = Stack[int](3)

# for num in range(5,8):
#     stack.push(num)
try:

    stack.push(5)
    stack.push(9)
    stack.push(11)
    
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()




except ValueError as e:
    print("error is ",e)

finally:
    print(" nomral tak")




print(stack.items)