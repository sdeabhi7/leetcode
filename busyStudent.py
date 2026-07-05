#   author: sdeabhi



def busyStudent(startTime, endTime, queryTime):
    value = 0
    for i, j in zip(startTime, endTime):
        if i <= queryTime <= j:
            value += 1
    return value

print(busyStudent([1,2,3], [3,2,7], 4))