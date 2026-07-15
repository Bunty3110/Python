# 59. Spiral Matrix II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0]*n for _ in range(n)]
        dx=1
        dy=0
        X=0
        Y=0
        for k in range(n*n):
            ans[Y][X]=k+1
            if not 0<=X+dx<n or not 0<=Y+dy<n or ans[Y+dy][X+dx]>0:
                dx,dy=-dy,dx
            X+=dx
            Y+=dy
        return ans

        
            

        