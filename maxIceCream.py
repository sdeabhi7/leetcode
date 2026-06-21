#   author: sdeabhi



def maxIceCream(costs, coins):
    value = 0
    costs.sort()
    for i in costs:
        if coins >= i:
            coins -= i
            value += 1
            if coins <= 0:
                return value
    return value

print(maxIceCream([1,3,2,4,1], 7))