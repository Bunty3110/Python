# 42. Trapping Rain Water
# Hard
# Topics
# premium lock icon
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

class Solution:
    def trap(self, height: List[int]) -> int:
        left =0
        right =len(height)-1
        lmax=height[left]
        rmax=height[right]
        water=0
        while left<right:
            if lmax<rmax:
                left+=1
                lmax=max(lmax,height[left])
                water+=lmax-height[left]
            else:
                right-=1
                rmax=max(rmax,height[right])
                water+=rmax-height[right]
        return water