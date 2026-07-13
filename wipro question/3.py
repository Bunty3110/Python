# sum of difference of array
def sumofdiff(arr):
    sum=0
    for i in range(len(arr)-1):
        sum=sum+(abs(arr[i]-arr[i+1]))
    return sum

arr= list(map(int,input().split()))
print(sumofdiff(arr))