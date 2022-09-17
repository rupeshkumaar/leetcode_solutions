# Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

class Solution:
    def isPalindrome(self,s):
        s = "".join([i.lower() for i in s if self.isalphanumeric(i)])
        right = len(s)-1
        for left in range(len(s)):
            if s[left] != s[right]:
                return False
            else:
                right -= 1
        return True

    def isalphanumeric(self,char):
        if ord ("A") <= ord(char) <= ord("Z") or \
            ord("a") <= ord(char) <= ord("z") or \
            ord('0') <= ord(char) <= ord("9"):
            return True
        return False
            

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("raceacar"))
