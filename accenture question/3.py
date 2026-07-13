def ratCount(rat, unit , arr,size):
    if arr is None:
        return -1
    total=rat*unit
    for i in range(size):
        total=total -arr[i]
        if(total<=0):
            return i+1
    if(total>0):
        return 0
    
rat=int(input())
unit= int(input())
size= int(input())
arr=list(map(int,input().split()))
answer=ratCount(rat,unit,arr,size)
print(answer)