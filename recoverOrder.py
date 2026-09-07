#   author: sdeabhi






def recoverOrder(order, friends):
    value = []
    for i in order:
        if i in friends:
            value.append(i)
    return value

print(recoverOrder([3,1,2,5,4], [1,3,4]))