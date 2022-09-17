# Encode and Decode Strings

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Example 1:
# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"

# Example 2:
# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

class Solution:
    def encode(self,strs):
        print("encdoing")
        result = ''
        for s in strs:
            result += s + "::"
        return result

    def decode(self,string):
        print("decoding")
        return [s for s in string.split("::") if s != '']

solution = Solution()
solution.encode(["lint","code","love","you"])
solution.decode(solution.encode(["lint","code","love","you"]))

