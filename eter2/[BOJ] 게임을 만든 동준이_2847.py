n = int(input())
score = []
for i in range(n):
    score.append(int(input()))

ans = 0
for i in range(n-2, -1, -1):
    if score[i] >= score[i+1]:
        ans += score[i] - score[i+1] + 1
        score[i] = score[i+1]-1

print(ans)