def sugarbags(N):
    # 5로 나눈 몫을 share 변수에 저장
    share = N // 5
    # N에서 5kg 봉투로 담은 후 남은 무게
    rest_weight = N % 5

    # 나머지가 0이면 바로 반환
    if rest_weight == 0:
        return share  # 5kg 봉투만으로 정확히 나눌 수 있음
    
    # 5kg 봉투로 최대한 담은 후 남은 무게를 3kg 봉투로 나눌 수 있는지 확인
    while share >= 0:
        if rest_weight % 3 == 0:
            # 3kg 봉투의 개수를 rest 변수에 저장
            rest = rest_weight // 3
            # 총 봉투 수를 반환
            return share + rest
        # 5kg 봉투의 개수를 줄이고, 남은 무게를 다시 계산
        share -= 1
        rest_weight += 5
    
    # 정확히 나눌 수 없는 경우
    return -1

N = int(input())
print(sugarbags(N))
