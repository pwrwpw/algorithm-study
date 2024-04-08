nums = [1,4,3,2]

nums.sort()

result = []

answer = 0

for i in range(len(nums)):
    result.append(nums[i])

    if len(result) == 2:
        answer += min(result)
        result = []

print(answer)