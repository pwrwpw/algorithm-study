array = [7,1,5,3,6,4]

cost = []

for i in range(len(array)):
    for j in range(len(array)):
        cost.append((j-i))

print(max(cost))