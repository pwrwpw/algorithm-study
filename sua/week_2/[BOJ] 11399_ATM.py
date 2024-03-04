n = int(input())  
wating = list(map(int, input().split()))  

wating.sort()  
tot = 0  

for i in range(1, n+1):
    tot += sum(wating[0:i])  
print(tot)