#INTERVIEW QUES)
# 1) DIFFERENCE BETWEEN LINEAR AND BINARY SEARCH

'''| Feature          | Linear Search                     | Binary Search                           |
| ---------------- | --------------------------------- | --------------------------------------- |
| Searching Method | Checks elements one by one        | Checks middle element and divides array |
| Data Requirement | Works on sorted and unsorted data | Requires sorted data                    |
| Speed            | Slower                            | Faster                                  |
| Time Complexity  | `O(n)`                            | `O(log n)`                              |
| Best For         | Small datasets                    | Large datasets                          |
| Implementation   | Simple                            | Slightly complex                        |
'''

# 2)BINARY SEARCH

'''ANS: 1.Binary search is faster than linear search 
2.Half of the remaining elements can be eliminated at a time, instead of eliminating them one by one
3.Binary search only works for sorted array'''

'''* BINARY SEARCH IN PYTHON

   BINARY SEARCH PSEUDOCODE ---  must know pseudocode

1. Create a function with 2 parameters:
   - a sorted array
   - a value to search

2. Create 2 pointers:
   - left pointer at the start of the array
   - right pointer at the end of the array

3. Repeat while left pointer is less than or equal to right pointer:
   
   a. Find the middle index
      middle = (left + right) // 2

   b. If middle element equals the value:
         return middle index

   c. If value is greater than middle element:
         move left pointer to middle + 1

   d. Else:
         move right pointer to middle - 1

4. If value is not found:
      return -1
'''
''' TIME COMPLEXITY = O(log N) '''

'''  USE EXAMPLE :  like find page number in a book'''

def binarySearch(array, target):
    low = 0
    high = len(array)-1
    while low<=high:
        mid = (low + high)//2   # mid = (low + high)/2 this will give float
        if array[mid]==target:
            return mid
        elif array[mid]< target:
            low = mid+1
        else:
            high = mid-1
    return -1        
array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
target = 72
result = binarySearch(array, target)
if result == -1:
    print("Element not found")
else:
    print("Element found at: ",result)    

#===============================================================================================
# SORTING
# BUBBLE SORT    

def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            print(array)
        print()

array = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(array)                

#========================================================================================

