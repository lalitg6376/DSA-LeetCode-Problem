class Solution:
    def lengthOfLastWord(self,s):
        j = len(s)-1
        count = 0
        while j >= 0 and s[j] == " ":
            j-=1
                
        while j >= 0 and s[j] != " ":
            count+=1
            j-=1
        return count
        
obj = Solution()
ans = obj.lengthOfLastWord("hello world")
print(ans)
