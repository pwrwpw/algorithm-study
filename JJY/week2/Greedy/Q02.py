data = input()

result = int(data[0])

for i in ragne(1, len(data)) : 
    num = int(data[1])
    if num <= 1 or result <= 1 :
        result += num
    else : 
        result *= num
        
print(result)