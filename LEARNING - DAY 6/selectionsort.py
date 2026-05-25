''''
Start from the first element of the array.
Assume the current element is the smallest.
Compare it with the remaining elements.
Find the actual smallest element in the unsorted part.
Swap it with the current element.
Move to the next position.
Repeat until the array is sorted.'''

# Selection Sort

arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):  # (0,4)
    min_index = i  # i = 0   min = 64
    for j in range(i + 1, len(arr)):  # j =(1,4)
        if arr[j] < arr[min_index]:  # 1 < 0  -- 25 < 64 
            min_index = j
    # swa
    arr[i], arr[min_index] = arr[min_index], arr[i]  # arr[0], arr[4] = arr[4], arr[0]
print("Sorted array:", arr)