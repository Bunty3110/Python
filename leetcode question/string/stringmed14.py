# 3557. Find Maximum Number of Non Intersecting Substrings
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string word.

# Return the maximum number of non-intersecting substrings of word that are at least four characters long and start and end with the same letter.

 

# Example 1:

# Input: word = "abcdeafdef"

# Output: 2

# Explanation:

# The two substrings are "abcdea" and "fdef".

# Example 2:

# Input: word = "bcdaaaab"

# Output: 1

# Explanation:

# The only substring is "aaaa". Note that we cannot also choose "bcdaaaab" since it intersects with the other substring.

 

# Constraints:

# 1 <= word.length <= 2 * 105
# word consists only of lowercase English letters
class Solution:
    def maxSubstrings(self, word: str) -> int:
        li=[]
        sub=0
        for i in range(len(word)):
            if word[i] in li :
                li.append(word[i])
                if len(li)-li.index(word[i])>3:
                    sub+=1
                    li=[]
            elif word[i] not in li:
                li.append(word[i])
        return sub
        