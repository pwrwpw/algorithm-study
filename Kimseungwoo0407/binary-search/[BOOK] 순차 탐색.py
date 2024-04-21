def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1 # 인덱스니까 + 1

input_data = input().split() # 5 Seungwoo
n = int(input_data[0])
target = input_data[1]

array = input().split() # Hyunseok Hyunyoung Sua Seungwoo Juyeong

print(sequential_search(n,target,array))