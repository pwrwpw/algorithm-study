n=int(input())
sales=[]
for i in range(n):
    sales.append(int(input()))
sales.sort(reverse=True)

free=0
for i in range(2,len(sales),3):
    free+= free[i]

print(sum(sales)-free)