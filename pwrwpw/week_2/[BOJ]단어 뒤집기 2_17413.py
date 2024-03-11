def reverse_words(sentence):
    parts = sentence.split('<')
    result = ''
    for part in parts:
        if '>' in part:

            tag, word = part.split('>', 1)
            result += '<' + tag + '>'
            words = word.split()
            for i in range(len(words)):
                result += words[i][::-1]
                if i < len(words) - 1:
                    result += ' '
        else:
            words = part.split()
            for i in range(len(words)):
                result += words[i][::-1]
                if i < len(words) - 1:
                    result += ' '
    return result

s = input()

print(reverse_words(s))
