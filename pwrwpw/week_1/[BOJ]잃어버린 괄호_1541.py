#시간복잡도 : O(N)

s = input().split('-')

answer = 0

for i in s[0].split('+'):
    answer += int(i)

for i in s[1:]:
    for j in i.split('+'):
        answer -= int(j)

print(answer)
