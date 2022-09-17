# 3sum

# Input: nums = [-1,0,1,2,-1,-4]
# // -1,-1,-1
# // -1,0,1
# // -1,1,-1
# // -1,2,-1
# // -1,-1,1
# // -1,-4,-1

# // 0,-1,1
# // 0,0,-1
# // 0,1,1
# // 0,2,-1
# // 0,-1,1
# // 0,-4,-1



# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

from collections import Counter

class Solution:
    def threeSum(self, nums):
        # nums = [-1, 0, 1, 2, -1, -4]
        nums.sort()
        res = []
        for i in range(len(nums)):
            m = i + 1
            r = len(nums)-1
            while m < r:
                sum = nums[i] + nums[m] + nums[r]
                if sum == 0 and [nums[i],nums[m],nums[r]] not in res:
                    res.append([nums[i],nums[m],nums[r]])
                    r -= 1
                elif sum < 0:
                    m += 1
                else:
                    r -= 1
        
        return res

solution = Solution()

print(solution.threeSum([-1,0,1,2,-1,-4]))

