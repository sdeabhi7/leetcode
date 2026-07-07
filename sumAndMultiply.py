#   author: sdeabhi



def sumAndMultiply(n):
    if n > 0:
        nums = str(n)
        value = 0
        k = ''
        for i in nums:
            if i != '0':
                k += i
                value += int(i)
        return int(k) * value
    else:
        return n
    
print(sumAndMultiply(10203004))