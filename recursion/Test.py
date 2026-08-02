


def subsets(arr,cur_index,cur_subset,all_subsets):

        if cur_index == len(arr):
                all_subsets.append(list(cur_subset))
                return 
        cur_subset.append(arr[cur_index])
        subsets(arr, cur_index+1,cur_subset,all_subsets)
        cur_subset.pop()
        subsets(arr, cur_index+1,cur_subset,all_subsets)


def persons(arr,index):
        if index == len(arr):
            return 0 
        else :
               return 1 +persons(arr,index+1)
        