# Number of Carries During Addition
# Problem Statement

# A carry occurs when the sum of digits during the addition of two numbers(performed from right-to-left, digit by digit) exceeds9, causing a digit to be carried over to the next higher place value.

# You are required to implement the following function:

# Function Signature
# int NumberOfCarries(int num1, int num2);
# The function accepts two non-negative integers num1 and num2 asinput. You are required to calculate and return the total number of carries generatedwhile adding the digits of the two numbers from right-to-left.

# Input
# ·       Two non-negative integers: num1 and num2.

# Output
# ·       Return an integer representing the total number of carries generatedduring the addition.

# Constraints
# ·       0 <=num1, num2 <= 10?

# Example
# Example 1
# Input:
# num1 = 451
# num2 = 349

# Output:
# 2

# Explanation:
# Adding the numbers digit-by-digit from right-to-left:

# ·       1 + 9 =10, carry 1

# ·       5 + 4 +1 (carry) = 10, carry 1

# ·       4 + 3 +1 (carry) = 8, no carry

# Total carries = 2.

# Example 2
# Input:
# num1 = 23
# num2 = 563

# Output:
# 0

# Explanation:
# Adding the numbers digit-by-digit:

# ·       3 + 3 =6, no carry

# ·       2 + 6 =8, no carry

# ·       0 + 5 =5, no carry

# Total carries = 0.

# Additional Test Cases
# Test Case 1
# Input:
# num1 = 555
# num2 = 555

# Output:
# 3

# Explanation:

# ·       5 + 5 =10, carry 1

# ·       5 + 5 +1 = 11, carry 1

# ·       5 + 5 +1 = 11, carry 1
# Total carries = 3.

# Test Case 2
# Input:
# num1 = 123
# num2 = 594

# Output:
# 1

# Explanation:

# ·       3 + 4 =7, no carry

# ·       2 + 9 =11, carry 1

# ·       1 + 5 +1 = 7, no carry
# Total carries = 1.

# Test Case 3
# Input:
# num1 = 0
# num2 = 0

# Output:
# 0
def numberOfCarries(num1,num2):
    count=0
    previous=0
    while(num2!=0 or previous!=0):
        a=num1%10
        b=num2%10
        num1=num1//10
        num2=num2//10
        sum= a+b+previous
        if (sum>9):
            count=count+1
            previous=1
        else:
            previous=0
    return count

num1=int(input())
num2=int(input())
carry=numberOfCarries(num1,num2)
print(carry)