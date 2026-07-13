# Difference of Sum
# Problem Statement

# You are required to implement the following function:

# def differenceofSum(n: int, m: int) -> int:
# The function accepts two integers n and mas arguments. You need to find:

# ·       The sum of all numbers in the range from 1to m (both inclusive) that are not divisible by n.

# ·       The sum of all numbers in the range from 1to m (both inclusive) that are divisible by n.

# Return the difference between the sum of numbers notdivisible by n and the sum of numbers divisibleby n.

# Input
# ·       n— A positive integer, representing the divisor.

# ·       m— A positive integer, representing the upper limit of the range (from 1 to m).

# Output
# ·       Return the difference between the sum of numbersnot divisible by nand the sum of numbers divisible by n.

# Constraints
# ·       n> 0 and m >0

# ·       The sum of numbers will lie within the integerrange.

# Example
# Example 1
# Input:
# n = 4, m = 20

# Output:
# 90

# Explanation:
# The sum of numbers divisible by 4 in the range 1 to 20:

# ·       4+ 8 + 12 + 16 + 20 = 60

# The sum of numbers not divisible by 4 in the range 1 to 20:

# ·       1+ 2 + 3 + 5 + 6 + 7 + 9 + 10 + 11 + 13 + 14 + 15 + 17 + 18 + 19 = 150

# The difference between these sums:

# ·       150- 60 = 90

# Example 2
# Input:
# n = 3, m = 10

# Output:
# 19

# Explanation:
# The sum of numbers divisible by 3 in the range 1 to 10:

# ·       3+ 6 + 9 = 18

# The sum of numbers not divisible by 3 in the range 1 to 10:

# ·       1+ 2 + 4 + 5 + 7 + 8 + 10 = 37

# The difference between these sums:

# ·       37- 18 = 19

def differenceofSum(n,m):
    sum1=0
    sum2=0
    for i in range(m+1):
        if(i%n==0):
            sum1=sum1+i
        else:
            sum2=sum2+i
    return abs(sum1-sum2)


n= int(input())
m=int(input())
print(differenceofSum(n,m))