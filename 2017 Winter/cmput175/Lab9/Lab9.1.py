import time
import random
def main():
    lst1=[300, 293, 286, 279, 272, 265, 258, 251, 244, 237, 230, 223, 216, 209, 202, 195, 188, 181, 174, 167, 160, 153, 146, 139, 132, 125, 118, 111, 104, 97, 90, 83, 76, 69, 62, 55, 48, 41, 34, 27, 20, 13, 6, 0]
    lst2=lst1[:]
    ## random the list 
    #random.shuffle(lst)
    print('The original list:',lst1)
    start1=time.time()
    # sort the lst1 by using the textbook selection sort method
    selectionSort(lst1)
    print('The sorted list:',lst1)
    end1=time.time()
    interval1=end1-start1
    print('The textbook selection sort used %10.7f seconds'%interval1)
    ## random the list 
    #random.shuffle(lst)
    print('The original list:',lst2)
    start2=time.time()
    # sort the lst2 by using the recursion selection sort method
    selection_sort(lst2,0,len(lst2))
    print('The sorted list:',lst2)
    end2=time.time()
    interval2=end2-start2
    print('The recursion selection sort used %10.7f seconds'%interval2)
    interval=abs(interval1-interval2)
    print('The differences between these two methods is %10.7f seconds'%interval)
    
    
def selectionSort(data):
    # -The textbook selection sort
    # go through the whole list
    for index in range(len(data)): 
        smallIndex = index
        # find the smallest element's index
        for i in range(index,len(data)):
            if (data[i]<data[smallIndex]): 
                smallIndex=i
        # swap the current element with the smallest element
        temp=data[index] 
        data[index]=data[smallIndex] 
        data[smallIndex]=temp
        
def selection_sort(lst,first,last):
    # -The recursion selection sort
    
    # find the smallest element
    myMin=first
    i=first
    while i<last:
        if lst[i]<lst[myMin]:
            myMin=i
        i+=1
    # if the min element is not on the first one then swap the two elements
    if myMin>first:
        temp=lst[myMin]
        lst[myMin]=lst[first]
        lst[first]=temp
        selection_sort(lst,first+1,last)
        
        
 
main()