# Sum of Numbers Divisible byBoth 3 and 5 in a Range
# Problem Statement

# You are required to implementthe following function:

# int Calculate(int m, int n);
# The function accepts twopositive integers m and n as its arguments. Your task is to calculate and return the sum of all numbers that are divisible by both 3 and 5 (i.e., divisible by 15) in the rangefrom m to n (inclusive).

# Input
# ·       Twointegers m and n, where 0 < m <= n

# Output
# ·       Returnthe sum ofnumbersdivisible by both 3 and 5 in the given range.

# Constraints
# ·       1 <= m <= n <= 106

# Example
# Example 1
# Input:
# m = 12
# n = 50

# Output:
# 90

# Explanation:
# The numbers divisible by both 3 and 5 between 12 and 50 are:

# ·       15

# ·       30

# ·       45

# Their sum is 15 +30 + 45 = 90.

# Example 2
# Input:
# m = 100
# n = 160

# Output:
# 510

# Explanation:
# The numbers divisible by 3 and 5 between 100 and 160 are:

# ·       105

# ·       120

# ·       135

# ·       150

# Sum = 105 + 120 + 135 + 150= 510.

# Example 3
# Input:
# m = 1
# n = 14

# Output:
# 0

# Explanation:
# There are no numbers between 1 and 14 divisible by both 3 and 5. So the outputis 0.

def numdivsum(m,n):
    sum=0
    for i in range(m,n+1):
        if(i%15==0):sum=sum+i
    return sum

m=int(input())
n=int(input())
print(numdivsum(m,n))