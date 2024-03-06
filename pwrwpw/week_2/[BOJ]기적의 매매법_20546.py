

def junHyun(money,stocks):
    stock = 0
    for i in range(len(stocks)):
        if money >= stocks[i]:
            while  money >= stocks[i]:
                money = money - stocks[i]
                stock += 1
    return money, stock

def sungMin(money,stocks):
    stock,up_count,down_count = 0,0,0
    for i in range(len(stocks)):
        if i < 13 and i > 0: #상승
            if stocks[i] < stocks[i+1]:
                up_count += 1
                down_count = 0
        if i < 13 and i > 0: #하락
            if stocks[i] > stocks[i+1]:
                up_count = 0
                down_count += 1
        if up_count >= 3: # 상승시 전량 매도
            while stock > 0:
                money += stocks[i]
                stock -= 1
        if down_count >= 3:
            while money >= stocks[i]:
                money -= stocks[i]
                stock += 1
    return money,stock


money = int(input())
stocks = list(map(int,input().split()))

junHyun_money,junHyun_stocks = junHyun(money,stocks)
sungMin_money,sungMin_stocks = sungMin(money,stocks)

junHyun_total = (stocks[-1] * junHyun_stocks) + junHyun_money
sungMin_total = (stocks[-1] * sungMin_stocks) + sungMin_money
if junHyun_total > sungMin_total:
    print("BNP")
elif junHyun_total == sungMin_total:
    print("SAMESAME")
else:
    print("TIMING")