# 28. Find the Index of the First Occurrence in a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pointer=0
        def check(haystack,needle,k):
            for i in range(len(needle)):
                if needle[i]!=haystack[k+i]:
                    return False
            return True
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                if check(haystack,needle,i):
                    return pointer
            pointer+=1
        return -1
        

        