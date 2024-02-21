n = int(input())
nums = list(map(int, input().split()))
prime = 0

for x in nums:
  for i in range(2, x+1):
    if x % i == 0:
      if x == i:
        prime += 1
      
      break

print(prime)