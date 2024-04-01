S = int(input())

result = 0
count = 0
i = 1
while result <= S:
    result += i
    count +=1
    i += 1
    if S-result < i:
        break

print(count)