#   author: sdeabhi

def processStr(s):
    value = ''
    for i in s:
        if i == '*':
            value = value[:-1]
        elif i == '#':
            value *= 2
        elif i == '%':
            value = value[::-1]
        else:
            value += i
    return value

print(processStr('a#b%*'))