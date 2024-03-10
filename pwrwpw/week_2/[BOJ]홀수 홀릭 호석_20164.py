def old_holic_hosuk(num, count):
    ans_max = 0
    ans_min = float('inf')

    # 현재 숫자에서 홀수를 카운트
    for digit in num:
        val = int(digit)
        if val % 2 != 0:
            count += 1

    # 숫자가 1개 일 때는 그냥 리턴
    if len(num) == 1:
        ans_min = ans_max = count
        return ans_min, ans_max

    # 숫자가 2개 일 때는 두 수를 합해서 재귀함수 호출
    elif len(num) == 2:
        val = sum(int(digit) for digit in num)
        return old_holic_hosuk(str(val), count)

    # 숫자가 3개 이상일 때
    else:
        # 3등분할 수 있는 모든 경우의 수를 다 해줌
        for i in range(len(num) - 2):
            for j in range(i + 1, len(num) - 1):
                s1 = num[:i + 1]  # 0 ~ i 까지
                s2 = num[i + 1: j + 1]  # i+1 ~ j까지
                s3 = num[j + 1:]  # j ~ 끝 까지
                total = int(s1) + int(s2) + int(s3)
                # 합한 수로 다시 재귀함수 호출
                val_min, val_max = old_holic_hosuk(str(total), count)
                # 최대 최솟값을 비교, 갱신
                ans_min = min(ans_min, val_min)
                ans_max = max(ans_max, val_max)

        return ans_min, ans_max


n = input()
answer_min, answer_max = old_holic_hosuk(n, 0)
print(answer_min, answer_max)
