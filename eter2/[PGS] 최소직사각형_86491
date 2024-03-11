def solution(sizes):
    w, h = 0, 0
    for i in sizes:
        tmp_w, tmp_h = 0, 0
        if i[0] <= i[1]:
            tmp_w = i[0]
            tmp_h = i[1]
        else:
            tmp_w = i[1]
            tmp_h = i[0]
        
        if tmp_w > w:
            w = tmp_w
        
        if tmp_h > h:
            h = tmp_h
            
    answer = w * h
    return answer