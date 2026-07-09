#   author: sdeabhi



def toGoatLatin(sentence):
    value = sentence.split()
    for i in range(len(value)):
        if value[i][0] in 'aieouAIEOU':
            value[i] += 'ma' + (i + 1) * 'a'
        else:
            value[i] = value[i][1:] + value[i][0] + 'ma' + (i + 1) * 'a'
    return ' '.join(value)

print(toGoatLatin('I speak Goat Latin'))