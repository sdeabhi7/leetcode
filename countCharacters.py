'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Constraints:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
'''

def countCharacters(words, chars):
    value = []
    t = {}
    for i in chars:
        if i not in t:
            t[i] = 1
        else:
            t[i] += 1  
    for i in words:
        m = 0
        k = t.copy()
        for j in i:
            if j in k and k[j] != 0:
                k[j] -= 1
                m += 1
            else:
                break
        if len(i) == m:
            value.append(i)
    return sum(len(i) for i in value)

print(countCharacters(["cat","bt","hat","tree"], "atach"))