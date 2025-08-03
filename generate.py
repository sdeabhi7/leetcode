'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
'''


def generate(numRows):
    value = []
    for i in range(numRows):
        r = [1] * (i + 1)
        for j in range(1, i):
            r[j] = value[i - 1][j] + value[i - 1][j - 1]
        value.append(r)
    return value

print(generate(5))