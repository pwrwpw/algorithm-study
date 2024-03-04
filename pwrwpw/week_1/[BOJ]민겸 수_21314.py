#시간 복잡도: O(N)

s = input()
m = 0

value = ['','']

for i in s:

    if i == 'M':
        m += 1
    else:
        if m:
            value[0] += str((10 ** m) * 5)
            value[1] += str((10 ** m) + 5)
        else:
            value[0] += '5'
            value[1] += '5'

        m = 0
if m:
    value[0] += '1' * m
    value[1] += str(10 ** (m - 1))

print('\n'.join(value))