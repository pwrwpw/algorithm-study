# 시간복잡도 : O(NlogN)

n = int(input())

time_list = [[0,0] for _ in range(n)]

for i in range(n):
    start,end = map(int,input().split())
    time_list[i] = (start,end)

time_list.sort(key = lambda x: (x[1],x[0]))

temp = time_list[0][1]
cnt = 1

for i in range(1,n):
    if time_list[i][0] >= temp:
        cnt += 1
        temp = time_list[i][1]

print(cnt)