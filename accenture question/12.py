# Large Small Sum
# Problem Statement

# You are required to implement the following function:

# def LargeSmallSum(arr: List[int]) -> int:
# The function accepts a list of integers arr. You are required to:

# Find the second largest element from the even positions (0th, 2nd, 4th, etc.) in the array.

# Find the second smallest element from the odd positions (1st, 3rd, 5th, etc.) in the array.

# Return the sum of these two elements.

# Input
# arr: A list of integers where the elements are unique.

# Output
# Return the sum of the second largest element from the even positions and the second smallest element from the odd positions.

# Constraints
# If the array is empty or has a length of 3 or less, return 0.

# Array elements are unique.

# Treat the 0th position as even.

# Array length is between 1 and 1000.

# Example
# Example 1
# Input:
# arr = [3, 2, 1, 7, 5, 4]

# Output:
# 7

# Explanation:

# Even-position elements: 3 (0th), 1 (2nd), 5 (4th)

# Second largest: 3

# Odd-position elements: 2 (1st), 7 (3rd), 4 (5th)

# Second smallest: 4

# The sum of the second largest from even positions and second smallest from odd positions:

# 3 + 4 = 7

# Example 2
# Input:
# arr = [1, 8, 0, 2, 3, 5, 6]

# Output:
# 8

# Explanation:

# Even-position elements: 1 (0th), 0 (2nd), 3 (4th), 6 (6th)

# Second largest: 3

# Odd-position elements: 8 (1st), 2 (3rd), 5 (5th)

# Second smallest: 5

# The sum of the second largest from even positions and second smallest from odd positions:

# 3 + 5 = 8

# Notes
# Return 0 if the array is empty or if its length is 3 or less.

# Ensure you are handling the positions correctly: even positions are 0, 2, 4, etc., and odd positions are 1, 3, 5, etc.
def summ(arr):
    even=[]
    odd=[]
    for i in range(len(arr)):
        if(i%2==0):
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    sum=even[-2]+odd[-2]
    return sum
    
arr=list(map(int, input().split()))
print(summ(arr))