
# Code
# Testcase
# Testcase
# Test Result
# 1260. Shift 2D Grid
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

# In one shift operation:

# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        total=n*m
        k%=total
        if not k: 
            return grid
        new=[[0]*n for _ in  range(m)]
        for i in range(m):
            for j in range(n):
                old_idx=i*n+j
                new_idx=(old_idx+k)%total
                new_row=new_idx//n
                new_col=new_idx%n
                new[new_row][new_col]=grid[i][j]
        return new
