# Problem Name: Missing Data

# Problem Statement

# One character is missing from the received string compared to the sent string.
# Identify and print the missing character.

# Input/Output Format
# Input:
# Two strings

# Output:
# Missing character

# Sample Input 1
# abcdfjgerj abcdfjger

# Sample Output 1
# j

# 5 Simplified Test Cases
# abcd abc ? d
# xyz xz ? y
# hello helo ? l
# a "" ? a
# mnop mnp ? o
def checkdiff(s,s2):
    for i in s:
        if i in s2:
            continue
        else:
            return i

s=input()
s2=input()
print(checkdiff(s,s2))