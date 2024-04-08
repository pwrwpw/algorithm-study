def solution(triangle):
    nums = [[0] * (len(triangle) + 1) for _ in range(len(triangle))]
    
    for i in range(len(triangle)):
        if i == 0:
            nums[i][0] = triangle[i][0]
            continue
        for j in range(len(triangle[i])):
            if j == 0:
                nums[i][j] = triangle[i][j] + nums[i-1][j]
            else:
                nums[i][j] = triangle[i][j] + max(nums[i-1][j-1], nums[i-1][j])
        
    answer = max(nums[len(triangle) - 1])
    return answer