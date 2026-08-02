from recursion.Test import subsets

data = [1,2,3]
cs= []
result=[]

subsets("abc",0,cs,result)

result=sorted(result,key=lambda x:len(x))

print("result is ",result)