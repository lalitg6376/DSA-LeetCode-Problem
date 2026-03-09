# Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self,haystack,needle):
        i = 0
        j = 0
        
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                
                if j == len(needle):
                    return i-j
            
            else:
                i = i-j+1
                j=0
        return -1
                
obj = Solution()          
ans = obj.strStr("sadbutsad","sad")
print(ans)
