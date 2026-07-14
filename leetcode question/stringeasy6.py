# 125. Valid Palindrome
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=""
        for i in s:
            if i.isalnum():
                p+=i
        p=p.lower()
        for i in range(len(p)//2):
            if p[i]!=p[-(i+1)]:
                return False
        return True