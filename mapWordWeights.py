#   author: sdeabhi



def mapWordWeights(words, weights):
    k = 'abcdefghijklmnopqrstuvwxyz'
    mapping = {i: chr(ord('z') - i) for i in range(26)}
    value = {}
    new_words = ''
    for i in range(26):
        value[k[i]] = weights[i] 
    for i in words:
        y = 0
        for j in i:
            y += value[j]
        t = y % 26
        new_words += mapping[t]
    return new_words

print(mapWordWeights(["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))