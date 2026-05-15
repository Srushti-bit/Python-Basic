salary = int(input("Enter your Salary: "))
rating = int(input("Enter yur performance appraisal rating: "))
increment = 0
if rating>=1 and rating <=3:
    increment = salary*10/100
elif rating>=3.1 and rating<=4:
    increment = salary*30/100
elif rating>4.1 and rating<=5:
    increment= salary*40/100
else:
    print('Invalid rating')
print('Increment Salary: ',increment+salary)     

#================================================================================================================

# basic salary = 20000
# so we have to calculate the 
# HRA of basic = 20%
# TA of basic = 30%
# DA of basic = 45%

# Calculate GrossSalary = ?

salary = 20000
GrossSalary = 0
if salary>0:
    HRA = salary*20/100
    TA = salary*30/100
    DA = salary*45/100
GrossSalary = salary + HRA + TA + DA    
print("GrossSalary: ",GrossSalary)  # 39000

#===========================================================================================

input = [5,7,8,3,7,8,9,2,3]
new_input =[]

for i in range (len(input)):
    count = 0
    key = input[i]
    j = i+1
    while j<len(input):
        if key == input[j]:
            new_input.append(key)
        j = j+1
print(len(new_input))          # ans: 3  

#------------------------------------------------------------------
input = [5,7,8,3,7,8,9,2,3]
new_input ={}

for i in range (len(input)):
    count = 0
    key = input[i]
    j = 1
    while j<len(input):
        if key == input[j]:
            count+=1
        j = j+1
        if count>1:
            new_input[key] = count
max = new_input            
print(max)   # ans: {7: 2, 8: 2, 3: 2}


