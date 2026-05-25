'''
1. Start from the second element of the array.

2. Store the current element in a temporary variable called `key`.

3. Compare the `key` with the elements before it.

4. If the previous element is greater than the `key`, move that element one position ahead.

5. Continue comparing until the correct position for the `key` is found.

6. Insert the `key` at its correct position.

7. Repeat the process for all elements in the array.

8. After all passes, the array becomes sorted.
'''

# Insertion Sort

arr = [5, 3, 8, 1, 2]

for i in range(1, len(arr)):
    key = arr[i]   #  arr[i] = 3 key = 3
    j = i - 1  #1-1=0
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]   # interchange 5 and 3's place [3,5,8,1,2]
        j -= 1  # 0-1 = -1  [5,5,8,1,2]
    arr[j + 1] = key  # [3,5,8,1,2]
print("Sorted array:", arr)

# tc = O(n^2)
# Mobile Apps
     # Sorting small contact lists, notifications, or messages.
# Gaming Software
    # Arranging player scores or rankings when only a few values change.
