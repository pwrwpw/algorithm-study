#END

n = int(input())
nums = list(map(int, input("").split()))
sum = 0

for num in nums : 
    cnt = 0
    if num > 1 : 
        for i in range(2, int(num**0.5)+1) : 
            if num % i == 0:
                cnt += 1
        if cnt == 0 : 
            sum += 1   
print(sum)
