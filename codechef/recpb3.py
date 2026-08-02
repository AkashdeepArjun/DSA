#  constrinat   2<= arr[i] <=40 , for all i arr[i] is distinct , 1<= target <=40
def combs(index,arr,target,current,result):

    if target==0:
        result.append(list(current))
        return

    if index == len(arr) or target < 0:
        return

    if arr[index] <= target :
        current.append(arr[index]) 
        new_target = target-arr[index]
        combs(index,arr,target=new_target,current=current,result=result)
        current.pop()

    
    combs(index+1,arr,target,current,result)









if __name__ == '__main__':

    data = [1,2,3,4,5,6]
    res = []
    curr=[]
    target = 4 

    combs(0,data,target,curr,res)

    print("hello there")

    print(res)