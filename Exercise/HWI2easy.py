x=int(input())
k=[]
for i in range(x):
    k.append(int(input()))
y=int(input())
for i in range(y):
    a,b,c,d =map(int, input().split())
    count=0
    for j in range(a,b+1):
        k[j]=c+count*d
        count+=1
    
print(sum(k))


