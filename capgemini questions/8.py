# find majority element in an array
def maxint(arr):
    maxele=arr[0]
    maxcount=1
    for i in arr:
        if arr.count(i)>maxcount:
            maxcount=arr.count(i)
            maxele=i
    if(maxcount>1):
        return maxele
    return -1
            
n=int(input())
arr=list(map(int,input().split()))
print(maxint(arr))