'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 
Constraints:
1 <= temperatures.length <= 10**5
30 <= temperatures[i] <= 100
'''

def dailyTemperatures(temperatures):
    n = len(temperatures)
    value = [0] * n
    sa = []
    for i, j in enumerate(temperatures):
        print(f'stack {sa}')
        # print(f'value {value}')
        while sa and sa[-1][0] < j:
            sa_j, sa_i = sa.pop()
            value[sa_i] = i - sa_i
        sa.append((j, i))
        print(f'sa[-1][0] {sa[-1][0]}')
    return value

print(dailyTemperatures([73,74,75,71,69,72,76,73]))

# def dailyTemperatures(temperatures):
#     n = len(temperatures)
#     value = [0] * n
#     for i in range(n):
#         for j in range(i+1, n):
#             if temperatures[j] > temperatures[i]:
#                 value[i] = j - i
#                 break
#     return value