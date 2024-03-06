s = input()
word = ''
result = ''
tag = False

for char in s:
    if char == '<':
        tag = True
        result += word[::-1] + char
        word = ''
    elif char == '>':
        tag = False
        result += char
    elif tag:
        result += char
    elif char == ' ':
        result += word[::-1]+char
        word = ''
    else:
        word += char

result += word[::-1]

print(result)