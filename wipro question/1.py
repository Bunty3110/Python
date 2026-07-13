# Problem Name: Security Key

# Problem Statement

# You are given a numeric data value used during secure transmission.
# Your task is to generate a security key, defined as the count of distinct digits that appear more than once in the number.

# If no digit is repeated, print -1.

# Input/Output Format
# Input:
# An integer value

# Output:
# An integer representing the security key

# Constraints
# 1 = Number of digits = 105

# Sample Input 1
# 578378923

# Sample Output 1
# 3


# Explanation
# Digits 7, 8, and 3 appear more than once.
# So, the security key is 3.

# 5 Simplified Test Cases
# Input: 12345
# Output: -1
# No repeating digits.

# Input: 112233
# Output: 3
# 1, 2, and 3 repeat.

# Input: 999
# Output: 1
# Only digit 9 repeats.

# Input: 101010
# Output: 2
# Digits 1 and 0 repeat.

# Input: 5
# Output: -1
# Single digit.

def security(s):
    a=list(s)
    duplicates=[]
    for i in a:
        if a.count(i)>1 and i not in duplicates:
            duplicates.append(i)
    if len(duplicates)<1:
        return -1
    return len(duplicates)
s=input()
print(security(s))
