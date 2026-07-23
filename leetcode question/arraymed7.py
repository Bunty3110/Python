# 40. Combination Sum II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=set()
        candidates.sort()
        def make(idx,comb,total):
            if total==target:
                res.add(tuple(comb[:]))
                return
            if total>target or idx>= len(candidates):
                return
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                make(i+1,comb,total+candidates[i])
                comb.pop()
        make(0,[],0)
        return [list(x) for x in res]