# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=max(nums) if nums else 0
        s=set(nums)
        for i in range(1,n):
            if i not in s:
                return i
        return 1 if n<=0 else n+1

         