'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2**31 <= matrix[i][j] <= 2**31 - 1
 
Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    r = [False] * m
    c = [False] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                r[i] = True
                c[j] = True
    for i in range(m):
        if r[i]:
            for j in range(n):
                matrix[i][j] = 0
    for j in range(n):
        if c[j]:
            for i in range(m):
                matrix[i][j] = 0
    return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))