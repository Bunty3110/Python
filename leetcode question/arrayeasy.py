# Example 1:

# Input: n = 4

# Output: 4

# Explanation:

# Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
# Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
# Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        esum=0
        osum=0
        for i in range(1,n*2+1):
            if i%2==0:
                esum+=i
            else:
                osum+=i
        return abs(esum-osum)
        