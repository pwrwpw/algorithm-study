n = int(input())
cards = list(map(int, input().split()))
m = int(input())
mine = list(map(int, input().split()))

cards.sort()

dic = {}

for card in cards:
  if x in dic:
    dic[x] += 1
  else:
    dic[x] = 1

for mine in mines:
  if x in dic:
    print(dic[x], end=' ')
  else:
    print('0', end= ' ')