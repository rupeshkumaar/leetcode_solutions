# Container With Most Water

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

class Solution:
    def maxArea(self, height):
        max_area = 0
        right = len(height) - 1
        for left in range(len(height)):
            while left < right:
                minimum = min(height[left],height[right])
                diff = max(left,right) - min (left,right)
                if diff == 0: diff = 1
                area = diff * minimum
                max_area = max(area,max_area)
                if height[right] == minimum:
                    right -= 1
                else:break
        return max_area

solution = Solution()

print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,1]))
print(solution.maxArea([1,2]))
print(solution.maxArea([2,3,4,5,18,17,6]))
