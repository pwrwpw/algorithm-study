
t = int(input())

def is_prime(value):
    if value < 2:
        return False
    for i in range(2,int(value**0.5)+1):
        if value % i == 0:
            return False
    return True


for _ in range(t):
    n = int(input())

    left_value , right_value = n//2, n//2

    while left_value > 0:
        if is_prime(left_value) and is_prime(right_value):
            print(left_value,right_value)
            break
        else:
            left_value -= 1
            right_value += 1
