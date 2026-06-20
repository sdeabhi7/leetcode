#   author: sdeabhi




def largestAltitude(gain):
    h = 0
    max_h = 0
    for i in gain:
        h += i
        max_h = max(h, max_h)
    return max_h

print(largestAltitude([-5,1,5,0,-7]))