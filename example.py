#  Reverse Each word in a string
# ques 1)  WAP to reverse each word in a string

#input: "Hello world"
# output: "olleH dlrow"

text = "Hello world"
result = " ".join(word[::-1] for word in text.split())
print(f'"{result}"')

#=================================================================================
# ques2)  Check for valid parenthesis

# WAp to check if a string containing () ia valid
#input: "((()))"
# output: valid

w = input("Enter parenthesis: ")
if "(" in w or ")" in w:
    if w.count("(") == w.count(")"):
        print('"Valid"')
    else:
        print('"Not valid"')
else:
    print('"Invalid input"')  

# w = input("enter parenthesis: ")
# if "(" in w or ")" in w:
#         if w.count("(") == w.count(")"):
#             print("valid")
#         else:
#             print("not valid")
# else: 
#         print("inavlid input")     
# 
#=================================================================================
#Find all duplicates in a list

# Ques 3) write a function to find all the elements that appear mor than once in a list
# input: [4,3,2,7,8,2,1,5,5]
# Output: [2,5]
# 
nums = [4,3,2,7,8,2,1,5,5]
duplicates = []
for i in nums:
    if nums.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)        

#=================================================================================

# sort dictionary by key or value:

# ques 4) write a function to sort a dictionary by keys or values in asc or desc order
# input: {"C":3,"B":2,"A":1}

data = {"C":3,"B":2,"A":1}
my_dict = dict(sorted(data.items()))
print(my_dict)  # ans: {'A': 1, 'B': 2, 'C': 3}

my_dict = dict(sorted(data.items(), reverse = True))
print(my_dict) # ans: {'C': 3, 'B': 2, 'A': 1}
