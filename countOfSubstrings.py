'''
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

Example 1:
Input: word = "aeioqq", k = 1
Output: 0

Explanation: There is no substring with every vowel.

Example 2:
Input: word = "aeiou", k = 0
Output: 1

Explanation: The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:
Input: word = "ieaouqqieaouqq", k = 1
Output: 3

Explanation: The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
 
Constraints:
5 <= word.length <= 2 * 105
word consists only of lowercase English letters.
0 <= k <= word.length - 5
'''

def countOfSubstrings(word, k):
        vowels = set("aeiou")
        n = len(word)
        result = 0
        
        next_consonant = [n] * n
        next_cons_index = n
        for i in range(n - 1, -1, -1):
            next_consonant[i] = next_cons_index
            if word[i] not in vowels:
                next_cons_index = i

        vowel_count = {}
        cons_count = 0
        left = 0  

        for right in range(n):
            ch = word[right]
            if ch in vowels:
                vowel_count[ch] = vowel_count.get(ch, 0) + 1
            else:
                cons_count += 1

            while cons_count > k and left <= right:
                left_ch = word[left]
                if left_ch in vowels:
                    vowel_count[left_ch] -= 1
                    if vowel_count[left_ch] == 0:
                        del vowel_count[left_ch]
                else:
                    cons_count -= 1
                left += 1

            while left <= right and cons_count == k and len(vowel_count) == 5:
                result += next_consonant[right] - right

                left_ch = word[left]
                if left_ch in vowels:
                    vowel_count[left_ch] -= 1
                    if vowel_count[left_ch] == 0:
                        del vowel_count[left_ch]
                else:
                    cons_count -= 1
                left += 1

        return result    
        
print(countOfSubstrings('ieaouqqieaouqq', 1))




# def countOfSubstrings(word, k):
#     vowel = 'aieou'
#     consonant = 'bcdfghjklmnpqrstvwxyz'
#     total = list(word)
#     value = 0
#     temp = 5 + k
#     for i in range(len(total)):
#         word_temp = word[i:temp+i]
#         vowel_count = sum(1 for i in word_temp if i in vowel)
#         consonant_count = sum(1 for i in word_temp if i in consonant)
#         if vowel_count == 5 and consonant_count == k:
#             value += 1
#     return value
        
# print(countOfSubstrings('aeioqq', 1))