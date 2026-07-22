# Roman to integer 
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
class Solution:
    def romanToInt(self, s: str) -> int:
        x=0
        flag=0
        for i in range(len(s)):
            if flag==1:
                flag=0
                continue
            if s[i]=="M":
                x+=1000
                flag=0
            elif s[i]=="D":
                x+=500
                flag=0
            elif s[i]=="C":
                if i+1<len(s):
                    if s[i+1]=="D":
                        x+=400
                        flag=1
                    elif s[i+1]=="M":
                        x+=900
                        flag=1
                    else:
                        x+=100
                        flag=0
                else:
                        x+=100
                        flag=0
            elif s[i]=="L":
                x+=50
                flag=0
            elif s[i]=="X":
                if i+1<len(s):
                    if s[i+1]=="L":
                        x+=40
                        flag=1
                    elif s[i+1]=="C":
                        x+=90
                        flag=1
                    else:
                        x+=10
                        flag=0
                else:
                        x+=10
                        flag=0
            elif s[i]=="V":
                x+=5
                flag=0
            elif s[i]=="I":
                if i+1<len(s):
                    if s[i+1]=="V":
                        x+=4
                        flag=1

                    elif s[i+1]=="X":
                        x+=9
                        flag=1
                    else:
                        x+=1
                        flag=0
                else:
                        x+=1
                        flag=0
        return x
