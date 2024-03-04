nums = set()

for value in range(2, 246914):
    is_prime = True
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            is_prime = False
            break
    if is_prime:
        nums.add(value)

while True:
    n = int(input())
    if n == 0:
        break
    answer = 0
    for num in range(n + 1, (2 * n) + 1):
        if num in nums:
            answer += 1
    print(answer)