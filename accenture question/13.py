# Decimal to N-Base Notation
# Problem Statement

# You are required to implement the following function:

# char* DectoNBase(int n, int num);
# The function accepts two positive integers n and num. You need to convert the decimal number num into its equivalent in base n and return the result as a string.

# Steps for Conversion:
# Divide the decimal number by n and treat the division as integer division.

# Write the remainder (in n-base notation) as a symbol.

# Divide the quotient again by n and treat the division as integer division.

# Repeat the above two steps until the quotient becomes 0.

# The n-base value is the sequence of remainders from last to first.

# Assumptions:
# 1 < n <= 36

# For values of the remainder:

# 0 to 9 corresponds to characters '0' to '9'.

# 10 to 35 corresponds to characters 'A' to 'Z'.

# Input
# n: A positive integer representing the base to which you need to convert (1 < n <= 36).

# num: A positive integer to be converted into base n.

# Output
# A string representing the number num in base n.

# Example
# Example 1
# Input:
# n = 12, num = 718

# Output:
# 4BA

# Explanation:

# Step 1: 718 ÷ 12 = 59 with remainder 10 (A in base 12).

# Step 2: 59 ÷ 12 = 4 with remainder 11 (B in base 12).

# Step 3: 4 ÷ 12 = 0 with remainder 4 (4 in base 12).

# The sequence of remainders (from last to first) is: 4, B, A, resulting in 4BA.

# Example 2
# Input:
# n = 21, num = 5678

# Output:
# CI8

# Explanation:

# Step 1: 5678 ÷ 21 = 270 with remainder 18 (I in base 21).

# Step 2: 270 ÷ 21 = 12 with remainder 18 (I in base 21).

# Step 3: 12 ÷ 21 = 0 with remainder 12 (C in base 21).

# The sequence of remainders (from last to first) is: C, I, 8, resulting in CI8.

# Constraints
# 1 < n <= 36

# num is a positive integer.

# The output should be returned as a string.d
def coded(n,num):
    digits='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    while(num>0):
        remainder=num%n
        result=digits[remainder]+result
        num=num//n
    return result

n=int(input())
num=int(input())
print(coded(n,num))