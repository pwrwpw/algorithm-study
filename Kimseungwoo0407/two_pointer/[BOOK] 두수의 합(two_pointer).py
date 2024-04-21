nums = [2,7,11,15]

target = 9

interval_sum = 0
end = 0

for start in range(len(nums)):
    while interval_sum < target and end < len(nums):
        interval_sum += nums[end]
        end +=1
    if interval_sum == target:
        print([start,end-1])
        break
    interval_sum -= nums[start]