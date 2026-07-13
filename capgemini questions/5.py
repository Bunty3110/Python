# find the largst element in array
n = int(input())
arr = list(map(int, input().split()))
largest = arr[0]
for k in arr:
    if k > largest:
        largest = k
print(largest)