def solution(n, computers):
    def dfs(idx):
        visited[idx] = 1
        for j in range(n):
            if visited[j] == 0 and computers[idx][j] == 1:
                dfs(j)
        
    answer = 0
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1
            
    return answer