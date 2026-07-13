# Perform Operation Based on Choice
# Problem Statement

# You are required to implement a function that performs a basic arithmetic operation (addition, subtraction, multiplication, or division) between two integers based on a given choice c.

# Function Signature
# int OperationChoices(int c, int a, int b);
# Input
# An integer c representing the operation to perform.

# Two positive integers: a and b as operands.

# Output
# Return the result of the operation based on the value of c.

# Operation Mapping
# If c == 1 ? Return a + b

# If c == 2 ? Return a - b

# If c == 3 ? Return a * b

# If c == 4 ? Return a / b

# Constraints
# 1 <= a, b <= 105

# 1 <= c <= 4

# It is guaranteed that division will result in an integer, and b ? 0 for c = 4.

# Example
# Example 1
# Input:
# c = 1
# a = 12
# b = 16

# Output:
# 28

# Explanation:
# Since c = 1, perform 12 + 16 = 28.

# Example 2
# Input:
# c = 2
# a = 16
# b = 20

# Output:
# -4

# Explanation:
# Since c = 2, perform 16 - 20 = -4.

# Example 3
# Input:
# c = 3
# a = 7
# b = 5

# Output:
# 35

# Example 4
# Input:
# c = 4
# a = 20
# b = 4

# Output:
# 5

# Notes
# You must handle the operations using only conditional or switch-case statements.

# Assume all operations result in valid integer output — no floating-point division is required.

# You may assume input values will always satisfy the conditions for safe division (i.e., b ? 0 when c == 4


c=int(input())
a=int(input())
b=int(input())
match c:
    case 1:
        c=a+b
        print(c)
    case 2:
        c=a-b
        print(c)
    case 3:
        c=a*b
        print(c)
    case 4:
        c=a/b
        print(c)




