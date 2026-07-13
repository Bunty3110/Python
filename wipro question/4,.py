# Problem Name: Odd Even Online Game

# Problem Statement

# Rearrange the array such that:

# All even numbers appear first

# All odd numbers appear next

# Maintain original order
def rearrange(arr):
    newarr=[]
    for i in range(len(arr)):
        if(arr[-(i+1)]%2==0):
            newarr.insert(0,arr[-(i+1)])
        if(arr[i]%2!=0):
            newarr.append(arr[i])
    return newarr

            
arr=list(map(int,input().split()))
print(rearrange(arr))