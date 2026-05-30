n=int(input())
A=[int(input())for _ in range(n)]
q=int(input())
tsum=0
for i in range(q):
    
    t,l,r=map(int, input().split())
    if(t==1):
        for j in range(l,r+1):
            A[j]=A[l]*(i-l+1)
    if(t==2):
        sum=0
        for j in range(l,r+1):
            sum+=A[j]
        tsum+=sum
print(tsum)

            
