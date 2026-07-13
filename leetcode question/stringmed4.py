# 6. Zigzag Conversion
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows>=len(s) or numRows==1:
            return s
        element=[[] for _ in range(numRows)]
        rowele=0
        mode=True
        new=""
        for i in s:
            element[rowele].append(i)
            if mode:
                rowele+=1
                if rowele==numRows:
                    mode=False
                    rowele-=2
            else:
                rowele-=1
                if rowele<0:
                    mode=True
                    rowele+=2
        for i in element:
            new+="".join(i)
        return new





        