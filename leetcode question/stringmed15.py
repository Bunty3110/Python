# 3775. Reverse Words With Same Vowel Count
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s consisting of lowercase English words, each separated by a single space.

# Determine how many vowels appear in the first word. Then, reverse each following word that has the same vowel count. Leave all remaining words unchanged.

# Return the resulting string.

# Vowels are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "cat and mice"

# Output: "cat dna mice"

# Explanation:​​​​​​​

# The first word "cat" has 1 vowel.
# "and" has 1 vowel, so it is reversed to form "dna".
# "mice" has 2 vowels, so it remains unchanged.
# Thus, the resulting string is "cat dna mice".
# Example 2:

# Input: s = "book is nice"

# Output: "book is ecin"

# Explanation:

# The first word "book" has 2 vowels.
# "is" has 1 vowel, so it remains unchanged.
# "nice" has 2 vowels, so it is reversed to form "ecin".
# Thus, the resulting string is "book is ecin".
# Example 3:

# Input: s = "banana healthy"

# Output: "banana healthy"

# Explanation:

# The first word "banana" has 3 vowels.
# "healthy" has 2 vowels, so it remains unchanged.
# Thus, the resulting string is "banana healthy".
class Solution:
    def reverseWords(self, s: str) -> str:
        word=s.split(" ")
        num=0
        sw=0
        for i in range(len(word)):
            count=0
            for j in word[i]:
                if j in "aeiou":
                    count+=1
            if sw==0:
                sw+=1
                num=count
                continue
            if num==count:
                word[i]=word[i][::-1]
        return " ".join(word)

        