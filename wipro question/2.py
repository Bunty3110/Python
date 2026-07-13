# You are given a number and a digit.
# Count how many times the given digit appears in the number.

# Input/Output Format
# Input:
# An integer N
# An integer D

# Output:
# Count of digit D in N

# Sample Input 1
# 572378233

# 3

# Sample Output 1
# 3


# Explanation
# Digit 3 appears three times in the number.

# 5 Simplified Test Cases
# Input: 1111 , 1 ? Output: 4
# Input: 90876 , 5 ? Output: 0
# Input: 12321 , 2 ? Output: 2
# Input: 0 , 0 ? Output: 1
def maxcount(s,n):
    return s.count(n)


s=input()
n=input()
print(maxcount(s,n))