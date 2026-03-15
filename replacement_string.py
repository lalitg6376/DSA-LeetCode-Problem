def replacement_string(s):
    s = list(s)
    i = 0
    j = len(s)-1
    replacement = 0
     
    while i < j:
        if s[i] == s[j]:
            i+=1
            j-=1
            
        elif s[i] != s[j]:
            s[j] = s[i]
            i+=1
            j-=1
            replacement+=1
    return replacement,s
            
ans = replacement_string("abca")
print(ans[0])
print(ans[1])
