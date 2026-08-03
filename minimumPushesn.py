#   author: sdeabhi



def minimumPushes(word):
    n = len(set(word))
    t = len(word)
    if n <= 8:
        return t
    elif n > 8:
        f = {}
        for i in word:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        f_values = sorted(list(f.values()), reverse=True)
        if 8 < n <= 16:
            return sum(f_values[:8]) + sum(f_values[8:16]) * 2 
        elif 16 < n <= 24:
            return sum(f_values[:8]) + sum(f_values[8:16]) * 2 + sum(f_values[16:24]) * 3 
        else:
            return sum(f_values[:8]) + sum(f_values[8:16]) * 2 + sum(f_values[16:24]) * 3 + sum(f_values[24:26]) * 4

print(minimumPushes('abcde'))