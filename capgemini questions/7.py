# Problem Statement:

# You are given two strings.

# Your task is to:
# Check whether the two strings are anagrams of each other.
# Two strings are anagrams if they contain the same characters with the same frequency.

# This problem is commonly used in Capgemini placement rounds to test frequency comparison logic.

# Input/Output Format:
# Input:
# First string
# Second string

# Output:
# Anagram or Not Anagram

# Constraints:
# 1 = Length of strings = 105

# Sample Input 1
# listen

# silent

# Sample Output 1
# Anagram
def checkAnagram(s,a):
    if sorted(s)==sorted(a):
        return 'Anagram'
    else:
        return 'Not Anagram'
s=list(input())
a=list(input())
print(checkAnagram(s,a))



# if freq array to be made then freq=[]*26  
# then for ch in s
#      i=ord(ch)-ord('a')
#      freq[i]+=1