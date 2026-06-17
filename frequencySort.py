#   author: sdeabhi



def frequencySort(s):
    freq, word = {}, ''
    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    sort_freq = dict(sorted(freq.items(), key=lambda a: a[1], reverse=True))
    for i, j in sort_freq.items():
        word += i * j
    return word

print(frequencySort('tree'))