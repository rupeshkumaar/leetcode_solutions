# Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

import collections

class Solution:
    def groupAnagram(self, strs):
        d = collections.defaultdict(list)
        for s in strs:
            d[str(sorted(s))].append(s)
        return d.values()

solution = Solution()
print(solution.groupAnagram(["eat","tea","tan","ate","nat","bat"]))

print(solution.groupAnagram([""]))


