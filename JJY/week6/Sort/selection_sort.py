# 백준 2750번 : 수 정렬하기(https://www.acmicpc.net/problem/2750)
# 선택정렬을 이용한 방식

data = []
minidx = 0

n = int(input())
for a in range(n) : 
    data.append(int(input()))
    
for i in range(len(data)-1) :           # 정렬하고자 하는 기준 i
    minidx = i                          # minidx를 i로 설정
    for j in range(i+1, len(data)) :    # i 이후의 친구들이랑 minidx를 비교
        if(data[minidx] > data[j]) :
            minidx = j
            
    data[minidx], data[i] = data[i], data[minidx] # 최종 결정된 minidx랑 바꿀 i를 스위치
                                                  # 따라서 한번 스위치 됨. 

for i in range(len(data))   :         
    print(data[i])