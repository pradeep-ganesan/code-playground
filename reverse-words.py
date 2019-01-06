def reverseWords(s):
    start = 0
    rev = ''
    for i, c in enumerate(s):
        word = None
        if i == len(s)-1:
            word = s[start:]
        elif ' ' != c:
            continue

        if not word:
            word = s[start:i]
        rev += ''.join(list(reversed(word))) + ' '
        start = i+1
    return rev[:-1]

print '\'{}\''.format(reverseWords('hello world it\'s my sentence'))
        