#   author: sdeabhi



def reformat(s):
    k = [i for i in s if i not in '1234567890']
    n = [i for i in s if i in '1234567890']
    value = ''
    if k and n and abs(len(k) - len(n)) <= 1:
        if len(k) > len(n):
            for i, j in zip(k,n):
                value += i + j
            return value + k[-1]
        elif len(k) < len(n):
            for i, j in zip(n,k):
                value += i + j
            return value + n[-1]
        else:
            for i, j in zip(n,k):
                value += i + j
            return value
    elif k and len(k) == 1:
        return k
    elif n and len(n) == 1:
        return n
    else:
        return ''
    
print(reformat('a0b1c2'))