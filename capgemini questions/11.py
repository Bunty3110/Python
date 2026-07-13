# Problem Name: Longest Substring with At Most K Distinct Characters





# Problem Statement:

# You are given a string and an integer K.
# Your task is to:
# Find the length of the longest substring that contains at most K distinct characters.

# This problem is commonly used in Capgemini placement rounds to test sliding window and HashMap logic.





# Input/Output Format:
# Input:
# A string
# An integer K

# Output:
# Length of the longest valid substring





# Constraints:
# 1 = Length of string = 105
# 0 = K = 26





# Sample Input 1
# abcba
# 2

# Sample Output 1
# 3

# Explanation:
# The substring bcb contains only 2 distinct characters and has maximum length.





# Sample Input 2
# aaaa
# 1

# Sample Output 2
# 4

# Explanation:
# All characters are the same, so the entire string is valid.





# 5 Simplified Test Cases:
# Input:
# abc
# 1

# Output:
# 1
# Only one distinct character allowed.

# Input:
# eceba
# 2

# Output:
# 3
# Substring ece is valid.

# Input:
# aabbcc
# 2

# Output:
# 4
# Substring aabb or bbcc.

# Input:
# abcdef
# 3

# Output:
# 3
# Maximum of three unique characters.

# Input:
# abc
# 0

# Output:
# 0
# No characters allowed.


