def EvenCount(arr):
    count=0
    for i in arr:
        if i%2==0:
            count=count+1
    return count

n= int(input())
arr= list(map(int, input().split()))
print(EvenCount(arr))