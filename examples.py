# find the max no of consecutive 1s in a binary array
# logic: iterate through the array, keeping track of the current 
# input: [1,1,0,1,1,1,0,1,1,1,1]
# output: 4

l= [1,1,0,1,1,1,0,1,1,1,1]
count = 0
max_count = 0

for num in l:
    if num==1:
        count+=1
        max_count= max(max_count, count)
    else:
        count = 0
print(max_count)        # ans: 4

#============================================================================================================

#Count substrings in a string
 #ques) WAP to count the number of occurences of a substring in a given string
 # logic: use loops to search for the substring and count occurences 
 # input: "abababab" and "ab"
 #output: 4

list_1 = "abababab"
list_2 =  "ab"
count = 0
i = 0
while i <= len(s) - len(sub):
    if s[i:i+len(sub)] == sub:
        count += 1
        i += len(sub)   # jump ahead (no overlap)
    else:
        i += 1
print(count)



#============================================================================================================

# WHILE LOOP

i = 1
while i<=5:
    print(i)
    i +=1
