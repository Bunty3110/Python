#  spiral order matrix
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
class Solution(object):
    def spiralOrder(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        ans=[]
        dx=1
        dy=0
        X=0
        Y=0
        for _ in range(n*m):
            ans.append(matrix[Y][X])
            matrix[Y][X] = "."

            if not 0<=X+dx<m or not 0<=Y+dy<n or matrix[Y+dy][X+dx]==".":
                dx,dy=-dy,dx
            X+=dx
            Y+=dy
        return ans

        