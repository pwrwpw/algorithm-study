nums = [0,1,0,2,1,0,1,3,2,1,2,1]

volume = 0

left,right = 0, len(nums) - 1

left_max, right_max = nums[left], nums[right]

while left < right:
    left_max, right_max = max(nums[left],left_max), max(nums[right],right_max) # 현재 가장 높은 벽을 의미

    if left_max <= right_max:
        volume += left_max - nums[left] # 왼쪽 기둥 최대 - 현재 높이
        left += 1
    else:
        volume += right_max - nums[right] # 오른쪽 기둥 최대 - 현재 높이
        right -=1

print(volume)