# 백준 2750번 : 수 정렬하기(https://www.acmicpc.net/problem/2750)
# 퀵정렬을 이용한 방식_일반

import sys
sys.setrecursionlimit(10**6)  # 재귀함수 깊이 늘려줌.

data = []

def quick_sort(array, start, end) :
    if start >= end : #원소 1개일 때 종료구문
        return
    pivot = int((start+end)/2)
    left = start+1
    right = end
    
    while left <= right :
        while left <= end and array[left] <= array[pivot] :
            left += 1
        
        while right > start and array[right] >= array[pivot] :
            right -= 1
        
        if left>right :
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[left], array[right] = array[right], array[left]
            
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

n = int(input())
for a in range(n) : 
    data.append(int(input()))
    
quick_sort(data, 0, len(data)-1)

for i in range(len(data))   :         
    print(data[i])