

n, k = map(int,input().split())
s = list(map(int,input().split()))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(k + 1):
        if s[i - 1] % 2 == 0:
            dp[i][j] = dp[i - 1][j] + 1
        else:
            if j > 0:
                dp[i][j] = dp[i - 1][j - 1]

max_length = 0
for i in range(1, n + 1):
    for j in range(k + 1):
        max_length = max(max_length, dp[i][j])

print(max_length)