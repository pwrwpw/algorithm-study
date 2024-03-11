def solution(answers):
    s_1 = [1, 2, 3, 4, 5]
    s_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    s_1_ans = 0
    s_2_ans = 0
    s_3_ans = 0
    for idx, i in enumerate(answers):
        if i == s_1[idx % 5]:
            s_1_ans += 1
        
        if i == s_2[idx % 8]:
            s_2_ans += 1
        
        if i == s_3[idx % 10]:
            s_3_ans += 1
        
    answer = []
    
    if s_1_ans > s_2_ans:
        if s_1_ans > s_3_ans:
            answer.append(1)
        
        if s_1_ans < s_3_ans:
            answer.append(3)
            
        if s_1_ans == s_3_ans:
            answer.append(1)
            answer.append(3)
            
    if s_1_ans < s_2_ans:
        if s_2_ans > s_3_ans:
            answer.append(2)
        
        if s_2_ans < s_3_ans:
            answer.append(3)
            
        if s_2_ans == s_3_ans:
            answer.append(2)
            answer.append(3)
    
    if s_1_ans == s_2_ans:
        if s_1_ans > s_3_ans:
            answer.append(1)
            answer.append(2)
        
        if s_1_ans < s_3_ans:
            answer.append(3)
            
        if s_1_ans == s_3_ans:
            answer.append(1)
            answer.append(2)
            answer.append(3)
        
    
    return answer