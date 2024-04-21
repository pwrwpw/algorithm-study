word = input()

data = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in data:
    word = word.replace(i, "A")

print(len(word))