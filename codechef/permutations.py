def make_num(number)->int:

    n=0
    for d in  number:

        n =10*n+d 


    return n




def permus(index ,target,arr,subset,final_result,final_numbers):

    if len(subset) == target:
        res = list(subset)
        final_result.append(res)
        final_numbers.append(make_num(subset))
        return

    if len(arr)-index < target:
        return

    if index == len(arr):
        return

    subset.append(arr[index])
    permus(index+1,target,arr,subset,final_result,final_numbers)

    subset.pop()

    
    permus(index+1,target,arr,subset,final_result,final_numbers)





if __name__ =='__main__':

    subset =[]
    final_result=[]
    index=0
    nums=[]
    print("enter data seprated by spaces")
    data=list(map(int,input().split()))

    target_length = int(input("enter length of digit you want to generate"))

    permus(index,target_length,data,subset,final_result,nums)

    print(final_result)

    print(nums)



    