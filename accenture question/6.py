# Maximum Exponent of 2 in a Range
# Problem Statement

# You are given two integers a and b, where a < b. Your task is to implement a function that returns the number between a and b (inclusive) which has the maximum exponent of 2 in its prime factorization.

# In other words, for each number i in the range [a, b], calculate the number of times i can be evenly divided by 2 (i.e., how many times it contains factor 2). Return the number which has the maximum such exponent.

# If two or more numbers in the range have the same maximum exponent of 2, return the smallest such number.

# Function Signature
# int MaxExponents(int a, int b);
# Input
# Two integers a and b, where a < b.

# Output
# Return the number between a and b (inclusive) that has the maximum exponent of 2.

# Constraints
# 1 <= a < b <= 105

# Example
# Example 1
# Input:
# a = 7
# b = 12

# Output:
# 8

# Explanation:
# Number of times each number is divisible by 2:

# 7 - 0

# 8 - 3 (8 - 4 - 2 - 1)

# 9 - 0

# 10 - 1

# 11 - 0

# 12 - 2

# 8 has the highest exponent of 2 (3 times). Hence, the output is 8.

# Example 2
# Input:
# a = 18
# b = 22

# Output:
# 20

# Explanation:

# 18 - 1 (18 - 9)

# 19 - 0

# 20 - 2 (20 - 10 - 5)

# 21 - 0

# 22 - 1

# 20 has the highest exponent of 2 (2 times).

# Example 3
# Input:
# a = 2
# b = 5

# Output:
# 4

# Explanation:

# 2 - 1

# 3 - 0

# 4 - 2

# 5 - 0

# 4 has the highest exponent of 2 (2 times).

def maxExponent(a,b):
    maxexp=0
    maxele=a
    for i in range(a,b+1):
        num=i
        count=0
        while(num!=0):
            if(num%2==1):break
            else: count=count+1
            num=num/2
        if(count>maxexp):
            maxexp=count
            maxele=i
    return maxele
        
a=int(input())
b=int(input())
print(maxExponent(a,b))