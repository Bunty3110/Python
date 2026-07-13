# Autobiographical Number
# Problem Statement

# An Autobiographical Number is a number N such that the first digit of N represents the count of how many 0s are present in N, the second digit represents the count of how many 1s are present in N, and so on.

# You are given the following function:

# def FindAutoCount(n: str) -> int:
# Task:
# The function accepts a string n representing a number and checks whether the number is an autobiographical number. If it is, return the count of distinct digits in the number. If it is not an autobiographical number, return 0.

# Assumptions:
# The input string n will not be longer than 10 characters.

# The input string will consist of numeric characters.

# If the input string is None, return 0.

# Input:
# n: A string representing a number (up to 10 characters long).

# Output:
# Return an integer, which is either:

# The count of distinct digits in the number if it is autobiographical.

# 0 if the number is not autobiographical.

# Constraints:
# The string n will contain only digits (0-9).

# The number must be valid according to the autobiographical property to be considered valid.

# Example:
# Example 1
# Input:

# n = "1210"
# Output:

# 3
# Explanation:

# The number 1210 satisfies the autobiographical property:

# The first digit 1 indicates there is 1 occurrence of the digit 0.

# The second digit 2 indicates there are 2 occurrences of the digit 1.

# The third digit 1 indicates there is 1 occurrence of the digit 2.

# The fourth digit 0 indicates there are 0 occurrences of the digit 3.

# Thus, the number is autobiographical, and the distinct digits present in 1210 are 0, 1, 2 (3 distinct digits).

# The function returns 3.

# Example 2
# Input:

# n = "2232"
# Output:

# 0
# Explanation:

# The number 2232 does not satisfy the autobiographical property:

# The first digit 2 indicates there are 2 occurrences of the digit 0, but there are no 0s in the number.

# The second digit 2 indicates there are 2 occurrences of the digit 1, but there is only 1 1 in the number.

# Hence, the number is not autobiographical.

# The function returns 0.

# Edge Case:
# If the string n is None:

# Input:

# n = None
# Output:

# 0
# Constraints:
# If the input string is None, return 0.

# If the number does not satisfy the autobiographical property, return 0.

# Return the count of distinct digits in the number if it is autobiographica
def FindAutoCount(s):
    if s is None: return 0 
    freq=[0]*10
    for i in s:
        freq[int(i)]+=1
    for i in range(len(s)):
        if freq[i]==int(s[i]):
            continue
        else:
            return 0
    count=0
    for i in freq:
        if i>0:
            count=count+1
    return count


s=input()
print(FindAutoCount(s))