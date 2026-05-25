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
print(max)   