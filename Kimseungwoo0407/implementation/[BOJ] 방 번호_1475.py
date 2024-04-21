n = input()

number = [0] * 10

for i in n:
    number[int(i)] +=1

a = number[6]+number[9]
number[6] = 0
number[9] = 0
b = max(number)
if a % 2 == 0:
    print(max(a//2,b))
else:
    print(max(a//2+1,b))

