def solution(n, times):
    left = 1
    right = max(times) * n
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        
        for time in times:
            tmp += mid // time
            
            if tmp >= n:
                break
        
        if tmp >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
            
    return answer