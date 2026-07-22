# 38. Count and Say
class Solution:
    def countAndSay(self, n: int) -> str:
        prev=[]
        for i in range(1,n+1):
            if i==1:
                prev=["1"]
                continue
            count=0
            num=prev[0]
            nex=[]
            for i in range(len(prev)):
                if prev[i]==num:
                    count+=1
                    if i+1==len(prev):
                        nex.append(str(count))
                        nex.append(num)
                else:
                    nex.append(str(count))
                    nex.append(num)
                    num=prev[i]
                    count=1
                    if i+1==len(prev):
                        nex.append(str(count))
                        nex.append(num)
            prev=nex
        prev= "".join(prev)
        return prev


