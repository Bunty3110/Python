# longest word in java 
def longestword(l):
    longest=""
    maxlen=0
    for i in l:
        if len(i)>maxlen:
            maxlen=len(i)
            longest=i
    return longest

s=input()
l=list(s.split())
print(longestword(l))
