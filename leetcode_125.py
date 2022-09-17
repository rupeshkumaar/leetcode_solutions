# Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i.lower() for i in s if self.isalphanumeric(i)])
        right = len(s)-1
        for i in range(len(s)):
            if s[i] != s[right]:
                return False
            else:
                right -= 1
        return True

    def isalphanumeric(self,char):
        if (ord('a') <= ord(char) <= ord('z') or
            ord('A') <= ord(char) <= ord('Z') or
            ord('0') <= ord(char) <= ord('9')):
            return True
        return False

solution = Solution()

print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome("ab_a"))


