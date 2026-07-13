# Characters from a String

# Problem Statement:

# You are given a string.

# Your task is to:
# Remove duplicate characters while maintaining the original order of characters.

# This problem is commonly used in Capgemini placement rounds to test frequency tracking and order preservation.

# Input/Output Format:
# Input:
# A string

# Output:
# String after removing duplicates

# Constraints:
# 1 = Length of string = 105

def removeduplicate(s):
    l=[]
    for i in s:
        if i in l:
            continue
        else:
            l.append(i)
    return ''.join(l)

s=input()
print(removeduplicate(s))