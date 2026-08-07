#   author: sdeabhi



def lemonadeChange(bills):
    f = 0
    t = 0
    for i in bills:
        if i == 5:
            f += 1
        elif i == 10 and f > 0:
            f -= 1
            t += 1
        else:
            if t > 0 and f > 0:
                t -= 1
                f -= 1
            elif f > 2:
                f -= 3
            else:
                return False
    return True

print(lemonadeChange([5,5,5,10,20]))