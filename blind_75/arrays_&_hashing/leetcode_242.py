# Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isValidAnagram(self, string1, string2):
        if len(string1) != len(string2):
            return False
        else:
            count1, count2 = {}, {}
            for char1,char2 in zip(string1,string2):
                count1[char1] = 1 + count1.get(char1,0)
                count2[char2] = 1 + count2.get(char2,0)
            
            return count1 == count2

solution = Solution()
print(solution.isValidAnagram('anagram','nagaram'))
print(solution.isValidAnagram('car','rat'))
print(solution.isValidAnagram('race','acer'))



