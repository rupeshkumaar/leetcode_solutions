# Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

class Solution:
    def containsDuplicate(self,nums):
        hashSet = set()
        for n in nums:
            if n not in hashSet:
                hashSet.add(n)
            else:
                return True
        return False

import random

nums = []
for _ in range(5):
    nums.append(random.randint(0,10))
print(nums)
solution = Solution()
print(solution.containsDuplicate(nums))
