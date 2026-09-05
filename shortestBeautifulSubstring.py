#   author: sdeabhi



def shortestBeautifulSubstring(s, k):
    if s.count('1') >= k:
        value, t = [], float('inf')
        y, a = '', ''
        for i in range(len(s)):
            if s[i] == '1':
                value.append(i)
        for i in range(len(value)):
            if i+k-1 < len(value):
                y = s[value[i]:value[i+k-1]+1]
                if len(y) < t:
                    t = len(y)
                    a = y
                elif len(y) == t and y < a:
                    a = y
        return a
    else:
        return ''

print(shortestBeautifulSubstring('100011001', 3))