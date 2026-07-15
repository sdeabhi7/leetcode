#   author: sdeabhi



def countBalls(lowLimit, highLimit):
    boxs = {}
    for i in range(lowLimit, highLimit+1):
        k = sum(int(j) for j in str(i))
        if k not in boxs:
            boxs[k] = 1
        else:
            boxs[k] += 1
    return max(boxs.values())

print(countBalls(1, 10))