# print first not repeating character of string
def firstnon(s):
    for i in s:
        if s.count(i)>1:
            continue
        else:
            return i
    return -1
s=input()
print(firstnon(s))