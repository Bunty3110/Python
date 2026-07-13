# Binary String Operations
# Problem Statement

# You are required to implement the following function:

# int OperationsBinaryString(char* str);
# The function accepts a string str as its argument. The string consists of binary digits (0 or 1) separated by alphabetic characters representing bitwise operations:

# 'A' denotes the AND operation.

# 'B' denotes the OR operation.

# 'C' denotes the XOR operation.

# You must scan the string from left to right, applying each operation in sequence (no operator precedence). Return the final result of all operations.

# Input
# A non-null binary string of odd length, alternating between digits (0 or 1) and operation characters (A, B, C).

# Output
# Return the final binary result (0 or 1) after evaluating the string from left to right.

# Return -1 if str is NULL or None.

# Constraints
# The string always begins and ends with a binary digit.

# The length of the string is always odd.

# Valid operation characters: 'A', 'B', 'C'

# All binary digits are either '0' or '1'.

# Example
# Example 1
# Input:
# str = "1C0C1C1A0B1"

# Output:
# 1

# Explanation:
# The expression translates to:
# 1 XOR 0 XOR 1 XOR 1 AND 0 OR 1
# Evaluating from left to right:

# 1 C 0 ? 1 ^ 0 = 1

# 1 C 1 ? 1 ^ 1 = 0

# 0 C 1 ? 0 ^ 1 = 1

# 1 A 0 ? 1 & 0 = 0

# 0 B 1 ? 0 | 1 = 1
# Final result: 1

# Example 2
# Input:
# str = "0C1A1B1C1C1B0A0"

# Output:
# 0

# Explanation:
# Evaluating left to right without precedence:
# 0 ^ 1 = 1
# 1 & 1 = 1
# 1 | 1 = 1
# 1 ^ 1 = 0
# 0 ^ 1 = 1
# 1 | 0 = 1
# 1 & 0 = 0
# Final result: 0

# Example 3
# Input:
# str = NULL

# Output:
# -1

# Explanation:
# Since the input string is NULL, the function returns -1.
def OperationBinaryString(op):
    if not op:
        return -1
    size=len(op)
    answer=int(op[0])
    for i in range(size-1):
        match op[i+1]:
            case 'A':
                answer=answer&int(op[i+2])
            case 'B':
                answer=answer|int(op[i+2])
            case 'C':
                answer=answer^int(op[i+2])
            case _:
                continue
    return answer
                

op=str(input())
print(OperationBinaryString(op))
