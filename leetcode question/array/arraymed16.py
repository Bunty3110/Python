# 1291. Sequential Digits
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans=[]
        l=len(str(low))
        def backtrack(num,i):
            if num>high:
                return
            if low<=num<=high:
                ans.append(num)
            if i>9:
                return
            backtrack(num*10+i,i+1)
        for s in range(1,10):
            backtrack(s,s+1)
        return sorted(ans)

            


        