# Problem Statement
# Find the number of trailing zeros in the factorial of a given number.

# Input/Output Format
# Input:
# An integer N

# Output:
# Number of trailing zeros in N!

# Sample Input 1
# 5

# Sample Output 1
# 1

# 5 Simplified Test Cases
# 3 ? 0
# 5 ? 1
# 10 ? 2
# 25 ? 6
# 100 ? 24

def factorial(n):
    if n==0:
        return 1;
    else:
        return n*factorial(n-1)
def countzero(n):
    count=0
    while(n):
        if(n%10==0):
            count+=1
            n=n//10
        else:
            break
    return count
n=int(input())
print(countzero(factorial(n)))

