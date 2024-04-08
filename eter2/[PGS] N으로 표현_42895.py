def solution(N, number):
    if number == N:
        return 1
    
    nums = []
    nums.append({N})
    for cnt in range(2, 9, 1):
        tmp = set()
        for i in range(cnt - 1):
            for j in nums[i]:
                for k in nums[-i-1]:
                    tmp.add(j+k)
                    tmp.add(j-k)
                    tmp.add(j*k)
                    if k != 0:
                        tmp.add(j//k)
        tmp.add(int(str(N) * cnt))
        if number in tmp:
            return cnt
        nums.append(tmp)
    return -1