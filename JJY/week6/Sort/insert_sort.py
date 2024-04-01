# 백준 2750번 : 수 정렬하기(https://www.acmicpc.net/problem/2750)
# 삽입정렬을 이용한 방식

# [ 5 , *2 , 3 , 4 , 1 ] 1번째 기준 시작
# [ 5 , *2 , 3 , 4 , 1 ] 1번째 기준 진행중 /5랑 2이랑 비교해 > 5가 더 크니까 뒤로가
# [ *2 , 5 , 3 , 4 , 1 ] 1번째 기준 완료

# [ 2 , 5 , *3 , 4 , 1 ] 2번째 기준 시작 /3뽑아
# [ 2 , *3 , 5 , 4 , 1 ] 2번째 기준 진행중 /5랑 3이랑 비교해 > 5가 더 크니까 뒤로가
# [ 2 , *3 , 5 , 4 , 1 ] 2번째 기준 진행중 /2랑 3이랑 비교해 > 3이 더 크니까 가만있어
# [ 2 ,  3 , 5 , 4 , 1 ] 2번째 기준 완료

data = []

n = int(input())
for a in range(n) : 
    data.append(int(input()))
    
    
for i in range(1, len(data)) : 
    for j in range(i, 0, -1) :
        if data[j] < data[j-1] : 
            data[j], data[j-1] = data[j-1], data[j]
        else : 
            break
        
for i in range(len(data))   :         
    print(data[i])