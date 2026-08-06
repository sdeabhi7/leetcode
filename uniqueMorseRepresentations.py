#   author: sdeabhi



def uniqueMorseRepresentations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    letters ='abcdefghijklmnopqrstuvwxyz'
    k = {}
    value = []
    for i, j in zip(letters, morse):
        k[i] = j
    for w in words:
        y = ''
        for l in w:
            y += k[l]
        if y not in value:
            value.append(y)
    return len(value)

print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))