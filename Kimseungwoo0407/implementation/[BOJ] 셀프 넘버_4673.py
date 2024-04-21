make = set()

for i in range(1,10000+1):
    if i < 10:
        make.add(i+i)
    else:
        a = i // 1000
        b = (i // 100) % 10
        c = (i //10) % 10
        d = i % 10
        make.add(i+a+b+c+d)
for j in range(1,10000+1):
    if j not in make:
        print(j)