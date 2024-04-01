def sum_digit(serial):
    return sum(int(ch) for ch in serial if ch.isdigit())

def insertion_sort(serials):
    for i in range(1, len(serials)):
        key = serials[i]
        j = i - 1
        while j >= 0:
            # 길이 비교
            if len(serials[j]) > len(key):
                serials[j + 1] = serials[j]
            elif len(serials[j]) == len(key):
                # 길이가 같을 경우 숫자 합 비교
                if sum_digit(serials[j]) > sum_digit(key):
                    serials[j + 1] = serials[j]
                elif sum_digit(serials[j]) == sum_digit(key):
                    # 숫자 합도 같을 경우 사전순 비교
                    if serials[j] > key:
                        serials[j + 1] = serials[j]
                    else:
                        # 현재 위치가 올바른 위치
                        break
                else:
                    # 현재 위치가 올바른 위치
                    break
            else:
                # 현재 위치가 올바른 위치
                break
            j -= 1
        serials[j + 1] = key
n = int(input())

arr = [input() for _ in range(n)]

insertion_sort(arr)

for index in arr:
    print(index)
