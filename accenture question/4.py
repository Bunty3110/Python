# 
def findCount(arr,size,num,diff):
    count=0
    for i in arr:
        comp=abs(num-i)
        if(comp<=diff):
            count=count+1
    if(count>0):
        return count
    else:
        return -1

arr=list(map(int, input().split()))
size=len(arr)
num=int(input())
diff=int(input())
answer=findCount(arr,size,num,diff)
print(answer)