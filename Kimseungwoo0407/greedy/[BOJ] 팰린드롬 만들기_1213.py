s = input()
char_count = {}
result = []
for char in s:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char] = 1
char_count_list = sorted(char_count.keys())
count = 0
for i in char_count:
    if char_count[i] % 2 == 1:
        count +=1

if len(s) % 2 == 0:
    if count > 0:
        print("I'm Sorry Hansoo")
    else:
        for i in char_count_list:
            while char_count[i] > 0:
                if char_count[i] >= 2:
                    char_count[i] -= 2
                    result.append(i)
        print(''.join(result)+''.join(result[::-1]))

elif len(s) % 2 == 1:
    if count != 1:
        print("I'm Sorry Hansoo")
    else:
        mid = ''
        for i in char_count_list:
            if char_count[i] % 2 ==1:
                mid = i
                char_count[i] -=1
            while char_count[i] > 0:
                if char_count[i] >= 2:
                    char_count[i] -= 2
                    result.append(i)
        print(''.join(result)+mid+''.join(result[::-1]))