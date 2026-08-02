#   author: sdeabhi



def minimumPushes(word):
    n = len(word)
    if n < 9:
        return n
    elif 8 < n < 17:
        return (n - 8) * 2 + 8
    elif 16 < n < 25:
        return (n - 16) * 3 + 8 * 2 + 8
    else:
        return (n - 24) * 4 + 8 * 3 + 8 * 2 + 8

print(minimumPushes('abcde'))