# Problem Name: Charlie Magic Mirror
# Problem Statement
# Given two strings, determine whether one string is a right rotation of the other.

# Return:

# 1 if true

# -1 otherwise

# Input/Output Format
# Input:
# Two strings

# Output:
# 1 or -1

# Sample Input 1
# sample plesam

# Sample Output 1
# 1

# 5 Simplified Test Cases
# abc bca ? 1
# abcd bcda ? 1
# abc acb ? -1
# a a ? 1
# abc ab ? -1

def check(li,li2):
    nli=[]
    for i in range(len(li)):
        if(i+1==len(li)):
            k=0
        else:
            k=i+1

        nli.append(li[k])
    if(li2==nli):
        return 1
    else :
        return -1

s=input()
s2=input()
li=list(s)
li2=list(s2)
print(check(li,li2))
