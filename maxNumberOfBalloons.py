'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:
1 <= text.length <= 10**4
text consists of lower case English letters only.
'''

def maxNumberOfBalloons(text):
    t = 'balloon'
    k = 0
    value = {}
    y = int(len(text)/len(t))
    for i in text:
        if i not in value:
            value[i] = 1
        else:
            value[i] += 1
    m = ''
    for i in range(y):
        for i in t:
            if i in value and value[i] > 0:
                value[i] -= 1
                m += i
                if m == t:
                    k += 1
                    m  = ''
    return k

print(maxNumberOfBalloons("nlaebolko"))