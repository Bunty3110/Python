# Move Hyphens to Front
# Problem Statement

# You are given a string strof length n,containing only alphabets and hyphens (-).
# Implement a function MoveHyphen(charstr[], int n) to move all hyphens (-)to the front of the string, while maintaining the order of theremaining characters.

# ·       If the input string str is null, return null.

# Function Signature
# char* MoveHyphen(char str[], int n);
# Input
# ·       A string str consisting of alphabets (a-z, A-Z) and hyphens (-).
# ·       An integer n representing the length of thestring.
# Output
# Return the updated string after moving allhyphens to the front.
# Constraints
# ·       1 <= n <= 105

# ·       strwill contain only alphabets and hyphen (-) characters.

# Example
# Example 1
# Input:
# str ="Move-Hyphens-to-Front"

# Output:
# "---MoveHyphenstoFront"

# Explanation:
# The given string contains 3 hyphens (-). After moving all hyphens to thefront, the rest of the characters maintain their original order.
 

def Movehyphen(s):
    hyphen=[]
    letters=[]
    for i in s:
        if (i=="-"): hyphen.append(i)
        else: letters.append(i)
    newstr=hyphen+letters
    return newstr

s=str(input())
answer=Movehyphen(s)
new_s=''.join(answer)
print(new_s)