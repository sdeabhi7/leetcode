def backspaceCompare(s, t):
    k, y = [], []
    for i in s:
        if i == '#' and len(k) != 0:
            del k[-1]
        elif i != '#':
            k.append(i)
    for i in t:
        if i == '#' and len(y) != 0:
            del y[-1]
        elif i != '#':
            y.append(i)
    return ''.join(k) == ''.join(y)

print(backspaceCompare('ab#c', 'ad#c'))