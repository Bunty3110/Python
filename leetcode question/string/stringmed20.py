# 567. Permutation in String
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        k=len(s1)
        for i in range(len(s2)-k+1):
            dummy=s2[i:i+k]
            if sorted(dummy)==s1:
                return True
        return False