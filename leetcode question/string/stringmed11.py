# 22. Generate Parentheses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:


# Input: n = 1
# Output: ["()"]
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(openp,closep,comb):
            if openp==closep and openp+closep==n*2:
                res.append(comb[:])
            if openp<n:
                dfs(openp+1,closep,comb+'(')
            if closep<openp:
                dfs(openp,closep+1,comb+')')
        dfs(0,0,"")
        return res
        