def main():
    my_lst=[1, 2, 10, 4, 5, 8, 7]
    #my_lst=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #my_lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    my_lst, inversions = count_inversions(my_lst)
    print(my_lst)
    print(inversions)
def count_inversions(my_lst):
    return mergeSort(my_lst)

def merge(left,right):
    result=[]
    i,j=0,0
    count=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            count+=len(left)-i
    result+=left[i:]
    result+=right[j:]
    return result,count

def mergeSort(lst):
    if len(lst)<=1:
        return lst,0
    middle=len(lst)//2
    left,l_count=mergeSort(lst[:middle])
    right,r_count=mergeSort(lst[middle:])
    result,t_count=merge(left,right)
    count=l_count+r_count+t_count
    return result,count
main()