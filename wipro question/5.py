# Problem Name: Lucky Customer





# Problem Statement

# A sequence starts as 1, 1.
# Each next number is the sum of the previous two numbers.
# Find the Nth number in the sequence.





# Input/Output Format
# Input:
# An integer N

# Output:
# Nth term of the sequence



# Sample Input 1

# 8

# Sample Output 1
# 21

# Explanation
# Sequence: 1 1 2 3 5 8 13 21



def lucky(n):
    if(n<=2):
        return 1
    zero=1
    one=1
    for i in range(n-2):
        sum = zero+one
        zero=one
        one=sum
    return one
n=int(input())
print(lucky(n))
