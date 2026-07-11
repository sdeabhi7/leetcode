#   author: sdeabhi



def numberOfSteps(num):
    value = 0
    while num >= 1:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        value += 1
    return value

print(numberOfSteps(14))