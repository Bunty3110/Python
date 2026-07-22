# 47. Permutations II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        def backtrack(idx):
            if idx==len(nums):
                ans.add(tuple(nums))
                return
            for i in range(idx,len(nums)):
                nums[i],nums[idx]=nums[idx],nums[i]
                backtrack(idx+1)
                nums[i],nums[idx]=nums[idx],nums[i]
        backtrack(0)
        return list(ans)