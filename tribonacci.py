#   author: sdeabhi



def tribonacci(n):
    value = [0,1,1]
    if n > 2:
        for i in range(3, n+1):
            if i != n:
                value.append(sum(value[-3:]))
            else:
                return sum(value[-3:])
    return value[n]

print(tribonacci(4))