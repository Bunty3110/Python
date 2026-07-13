# Given an array of prices, count how many pairs exist such that the difference between the pair equals K.

# Input/Output Format
# Input:
# Integer N
# Integer K
# N space-separated integers

# Output:
# Number of valid pairs

# Sample Input 1
# 6

# 13

# 10 15 23 14 2 15

# Sample Output 1
# 3
def answer(diff, arr, n):
    freq = {}
    count = 0

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in arr:
        if num + diff in freq:
            count += freq[num + diff]

    return count


n = int(input())
diff = int(input())
arr = list(map(int, input().split()))

print(answer(diff, arr, n))