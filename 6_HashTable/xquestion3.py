def first_non_repeating_char(words):
    dict={}
    for i in words:
        if i in dict:
            dict[i]=1   
        else:
            dict[i]=0
    for i in words:
        if dict[i]==0:
            return i 
    return None



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""