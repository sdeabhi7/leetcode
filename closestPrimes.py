'''
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, 
return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 
Constraints:
1 <= left <= right <= 106
'''

from math import sqrt
def closestPrimes(left, right):
    prime_list = []
    for i in range(left, right + 1):
        if i < 2:
            continue  

        prime_flag = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                prime_flag = False  
                break
        if prime_flag:
            prime_list.append(i)

    if len(prime_list) < 2:
        return [-1, -1]

    min_diff = float('inf')
    closest_pair = (-1, -1)

    for i in range(len(prime_list) - 1):
        diff = prime_list[i + 1] - prime_list[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (prime_list[i], prime_list[i + 1])
    return list(closest_pair)

print(closestPrimes(19, 31))
