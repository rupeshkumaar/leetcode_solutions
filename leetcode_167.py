# Two Sum II - Input Array Is Sorted

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

class Solution:
    def twoSum(self, numbers, target):
        d = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in d:
                return [d[diff],i+1]
            else:
                d[numbers[i]] = i+1

solution = Solution()

print(solution.twoSum([2,7,11,15],9))
print(solution.twoSum([-1,0],-1))
print(solution.twoSum([2,3,4],6))
