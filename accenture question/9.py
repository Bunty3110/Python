# Swap Characters in a String
# Problem Statement

# You are given a string str of length n, and two characters ch1 and ch2.
# Implement a function that replaces all occurrences of ch1 in the string with ch2, and all occurrences of ch2 with ch1.

# Function Signature
# void* ReplaceCharacter(char str[], int n, char ch1, char ch2);
# Input
# A character array str of length n, containing only lowercase English letters.

# Two characters ch1 and ch2 to be swapped.

# Output
# Return the modified string after swapping all occurrences of ch1 with ch2 and vice versa.

# If the input string is null, return null.

# If both characters are not present in the string or ch1 == ch2, return the string unchanged.

# Constraints
# 1 <= n <= 105

# str contains only lowercase English letters.

# ch1, ch2 are lowercase letters: 'a' to 'z'.

# Example
# Example 1
# Input:
# str = "apples"
# ch1 = 'a'
# ch2 = 'p'

# Output:
# "paales"

# Explanation:

# All 'a' are replaced with 'p' ? "p[pples]"

# All 'p' are replaced with 'a' ? "paales"

# Example 2
# Input:
# str = "hello"
# ch1 = 'h'
# ch2 = 'o'

# Output:
# "oellh"

# Example 3
# Input:
# str = "banana"
# ch1 = 'x'
# ch2 = 'y'

# Output:
# "banana"

# Explanation:
# Neither 'x' nor 'y' is present in the string, so the string remains unchanged.

# Example 4
# Input:
# str = "test"
# ch1 = 'e'
# ch2 = 'e'

# Output:
# "test"

# Explanation:
# Since ch1 and ch2 are the same, no changes are made.

def replaceCharacter(s,o,n):
    new=[]
    for i in range(len(s)):
        if(s[i]==n):
            new.append(o)
        elif(s[i]==o):
            new.append(n)
        else:
            new.append(s[i])
    new=''.join(new)
    return new
    


s=input()
o=input()
n=input()
print(replaceCharacter(s,o,n))