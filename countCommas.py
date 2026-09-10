#   author: sdeabhi



def countCommas(n):
    return max(n-999, 0)
print(countCommas(1002))

# def countCommas(n):
#     return sum(1 for i in range(1000, n+1)) if n >= 1000 else 0