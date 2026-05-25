# Remove leading Zeros from a list of integers
# Ques) Write a function to remove leading zeros from a list of integers
# i/o = [0,0,1,2,0,3,0,0,4]

num =  [0,0,1,2,0,3,0,0,4]
i = 0
while i<len(num) and num[i] == 0:
        i+=1
result = num[i:]
print(result)  # ans: [1, 2, 0, 3, 0, 0, 4]

# or

def remove_leading_zeros(nums):
    i = 0
    
    while i < len(nums) and nums[i] == 0:
        i += 1
    
    return nums[i:]
nums = [0,0,1,2,0,3,0,0,4]
print(remove_leading_zeros(nums))

#==========================================================================

# Find the first missing positive integer

# Ques) write a function to find missing positive integer in a list of unsorted integers

# i/o = [3,4,-1,1]
# o/p = 2


def first_missing_positive(nums):
    num_set = set(nums)   # Converts the list into a set
    i = 1
    while i in num_set:
        i += 1
    
    return i
nums = [3, 4, -1, 1]
print(first_missing_positive(nums))  # ans: 2

#==========================================================================

''' 
# EXCEPTION HANDLING: 

* TYPES OF ERROR:
  1) RUNTIME ERROR
  2) COMPILE TIME ERROR

  INTERVIEW QUES:

1) WHAT IS RUNTIME ERROR? AND HOW IT IS HANDLED  

Log data is commonly used to manage and debug runtime errors.

In real-world applications:

runtime errors are usually recorded in log files so developers can analyze and fix issues later. 


2) Why Do We Need User-Defined Exceptions?

User-defined exceptions improve code readability, maintainability, and help handle business rules more meaningfully. 
They allow developers to define specific error types for custom scenarios.'''


try:
     a = int(input("enter 1st number: "))
     b = int(input("enter 2nd number: "))
     print(a/b)
except ZeroDivisionError:
     print("invalid")     
except ValueError:
     print("enter only integer value: ")  
except:
     print("ABC")   
else:
     print("everything is ok")       
#or

try:
     a = int(input("enter 1st number: "))
     b = int(input("enter 2nd number: "))
     print(a/b)
except (ZeroDivisionError, ValueError) as msg:
     print("invalid")

''''
* Finally --

    depends on requirement
    eg: in netbanking -if we close the tab once then if we again visit netbanking site we need to login in again. 

'''     

try:
     a = int(input("enter 1st number: "))
     b = int(input("enter 2nd number: "))
     print(a/b)
except ZeroDivisionError:
     print("invalid")     
except ValueError:
     print("enter only integer value: ")  
except:
     print("ABC")   
else:
     print("everything is ok")  
finally("i always execute.")     