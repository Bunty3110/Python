# 3. Longest Substring Without Repeating Characters
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=[]
        size=0
        for i in s:
            if i not in sub:
                sub.append(i)
                size=max(len(sub),size)
            else:
                l=sub.index(i)
                sub=sub[l+1:]
                sub.append(i)
                size=max(len(sub),size)
        return size


     