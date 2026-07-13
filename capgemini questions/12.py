# Problem Name: Detect Duplicate Transaction IDs
# Problem Statement:

# You are given a list of transaction IDs.
# Your task is to:
# Check whether any duplicate transaction ID exists.
# Print Yes if duplicate is found, otherwise No.

# This problem simulates real-world transaction validation systems.

# Input/Output Format:
# Input:
# An integer N
# N space-separated integers

# Output:
# Yes or No

# Constraints:
# 1 = N = 105

# Sample Input 1
# 5
# 10 20 30 10 40

# Sample Output 1
# Yes

# Explanation:
# Transaction ID 10 appears more than once.

# Sample Input 2
# 3
# 1 2 3

# Sample Output 2
# No

# Explanation:
# All transaction IDs are unique.

# 5 Simplified Test Cases:
# Input:
# 1
# 5

# Output:
# No
# Only one transaction.

# Input:
# 4
# 7 8 9 7

# Output:
# Yes
# Duplicate exists.

# Input:
# 3
# 0 0 0

# Output:
# Yes
# All duplicates.

# Input:
# 5
# 1 2 3 4 5

# Output:
# No
# Unique IDs.

# Input:
# 2
# 99 9

# Output:

# Yes
# Same values.
n = int(input())
arr = list(map(int, input().split()))
s = set()
d = False
for num in arr:
    if num in s:
        d = True
        break
    s.add(num)
if d:
    print("Yes")
else:
    print("No")