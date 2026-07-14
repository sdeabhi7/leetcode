#   author: sdeabhi



def numOfStrings(patterns, word):
    return sum(1 for i in patterns if i in word)

print(numOfStrings(["a","abc","bc","d"], 'abc'))