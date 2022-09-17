# Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    def topKFrequent(self,nums,k):
        frequency_dict = {i:[] for i in range(len(nums),0,-1)}
        count_dict = {}
        for i in range(len(nums)):
            count_dict[nums[i]] = 1 + count_dict.get(nums[i],0)
        for key in count_dict:
            frequency_dict[count_dict[key]].append(key)
        result = []
        for key in frequency_dict:
            if len(result) >= k: break
            if len(frequency_dict[key][:k]) >= k:
                return frequency_dict[key][:k]
            else:
                result.extend(frequency_dict[key][:k])
        
        return result[:k]


solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3],2))
print(solution.topKFrequent([1],1))
print(solution.topKFrequent([-1,-1],1))

