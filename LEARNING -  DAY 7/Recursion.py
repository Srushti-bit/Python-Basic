'''
Recursion    V IMP

 INTERVIEW QUESTION:

  Ques 1) when we use recursion?

  - when main problem can be divided into similar sub problem

  - Like in tree we have to perfom bfs dfs there we have to perform recursion

  - uses stack memory , that's why we avoid recursion.

  Ques 2) Comparsion between iteration and recursion?

  - recursion is not space efficient ; iteration is space efficient : no stack memory require in case of iteration
  - recursion is not time efficient ; iteration is time efficient :  in case of recursion system needs more time for pop and elements to stack memory which makes recursion less time efficient
  - recursion- easy to code ; iteration- no easy to code

  #  Recursion must have base condition otherwise it will run infinite time


* MASTER TEMPLATE   |
--------------------

Almost every backtracking problem follows:

def backtrack(...):

    if solution_found:
        save_answer
        return

    for choice in choices:

        make_choice

        backtrack(smaller_problem)

        undo_choice
'''

def factorial(num):
    if num  <= 1:   # base condition
        return 1 
    return num * factorial(num - 1)
print(factorial(4)) 


# 4*factorial(3)
# 3*factorial(2)
# 2*factorial(1)
# 4*3*2*1 = 24

#------------------------------------------------------------------------------------------------------------------------
# capitalizeFirst Solution using recursion

def capitalizeFirst(arr): # 1st iteration: ['car', 'taco', 'banana'] ; 2nd iteration: ['taco', 'banana'] ; 3rd iteration: ['banana'] 
    result = []  # ['Car', 'Taco', 'Banana']
    if len(arr) == 0:
        return result
    
    result.append(arr[0][0].upper() + arr[0][1:])  # C+ar
                         # Col= 012    
                    # Row: 0 =  car
    return result + capitalizeFirst(arr[1:]) # now the arr which will pass will have the remaining ones to avoid repition
print(capitalizeFirst(['car', 'taco', 'banana']))  # ans:['Car', 'Taco', 'Banana']

#------------------------------------------------------------------------------------------------------------------------
# power  Calculation

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent -1)

print(power(2,0)) # 1
print(power(2,2)) # 4
print(power(2,4)) # 16

#------------------------------------------------------------------------------------------------------------------------
# productofArray solution

def productofArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productofArray(arr[1:])  # arr[0] → first element
# arr[1:] → remaining elements
# Multiplies first element with recursive result
    # 1*2*3*1 = 6

print(productofArray([1,2,3])) 
print(productofArray([1,2,3,10]))

#------------------------------------------------------------------------------------------------------------------------
# Reverse a string using recursion

def reverse(string):
    if len(string) <= 1:
        return string
    return string[len(string)-1] + reverse(string[0:len(string)-1])
          #  n + reverse(ohtyp)
          #  n + o + reverse(htyp)
          #.
          #.
print(reverse('python')) # nohtyp
print(reverse('appmillers'))

#------------------------------------------------------------------------------------------------------------------------
 # Recursive range

def recursiveRange(num): # 6
    if num <= 0:  # 6 <= 0 
        return 0
    return num + recursiveRange(num - 1) # 6 + 5
print(recursiveRange(6)) #6+5+4+3+2+1 = 21

#------------------------------------------------------------------------------------------------------------------------
# pallindrome string

def isPallindrome(string):
    if len(string) == 0:
        return True
    if string[0] != string[len(string)-1]:
        return False
    return isPallindrome(string[1:-1]) # a = a
# print(isPallindrome('awesome')) # False
# print(isPallindrome('foobar')) # False
print(isPallindrome('tacocat')) # true

#------------------------------------------------------------------------------------------------------------------------

# someRecursive Solution

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not (cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True
def isOdd(num):
    if num%2 == 0:
        return False
    else:
        return True
    
print(someRecursive([1,2,3,4], isOdd))    
print(someRecursive([4,6,8,9], isOdd)) 
print(someRecursive([4,6,8], isOdd)) 