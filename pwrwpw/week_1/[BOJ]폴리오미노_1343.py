# 시간복잡도 : 0(N)

boards = input()

idx = 0
new_boards = []

while idx < len(boards):
    if boards[idx:idx+4] == 'XXXX':
        new_boards.append('AAAA')
        idx += 4
    elif boards[idx:idx+2] == 'XX':
        new_boards.append('BB')
        idx += 2
    elif boards[idx] == 'X':
        new_boards = ['-1']
        break
    else:
        new_boards.append(boards[idx])
        idx += 1

print(''.join(new_boards))