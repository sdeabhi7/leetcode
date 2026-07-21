#   author: sdeabhi





def shiftGrid(grid, k):
    value = []
    r = len(grid[0])
    for i in grid:
        value.extend(i)
    n = len(value)
    y = k % n
    s = value[n-y:] + value[:n-y]
    t = []
    h = []
    for i in s:
        h.append(i)
        if len(h) == r:
            t.append(h)
            h = []
    return t

print(shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1))