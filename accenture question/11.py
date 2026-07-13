# Password Checker
# Problem Statement

# You are required to implement the following function:

# int CheckPassword(char str[], int n);
# The function accepts:

# A string str[] of size n representing a password input.

# Your task is to return:

# 1 if the password is valid.

# 0 if the password is invalid.

# A password is considered valid if it satisfies all of the following conditions:
# Contains at least 4 characters.

# Contains at least one numeric digit (0-9).

# Contains at least one uppercase letter (A-Z).

# Does not contain any space ' ' or forward slash '/'.

# The first character of the string must not be a digit.

# Input
# str — A non-empty string representing the password.

# n — The length of the string.

# Output
# Return 1 if the password is valid.

# Return 0 if the password is invalid.

# Constraints
# The input string will not be empty.

# The string may contain letters, digits, and special characters (except space and slash which are explicitly disallowed).

# Maximum length of the string = 1000 characters.

# Examples
# Example 1
# Input:
# str = "aA1_67"
# n = 6

# Output:
# 1

# Explanation:

# Length = 4 

# Contains digit 1 

# Contains uppercase letter A 

# No space or / 

# First character is not a digit 
# Password is valid.

# Example 2
# Input:
# str = "a987 abC012"
# n = 11

# Output:
# 0

# Explanation:

# Contains space ' ' ?
# Password is invalid.

# Example 3
# Input:
# str = "1abcA"
# n = 5

# Output:
# 0

# Explanation:

# First character is a digit '1' ?
# Password is invalid.

def checkpwd(s,n):
    for i in range(n):
        if(s[i]==' '):
            return 0
    return 1
s=input()
n=int(input())
print(checkpwd(s,n))