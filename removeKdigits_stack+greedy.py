class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for i in num:
            while stack and k > 0 and i < stack[-1]:
                stack.pop()
                k-=1
            stack.append(i)
            
        while k > 0:
            stack.pop()
            k-=1
                
        answer = "".join(stack)
            
        answer = answer.lstrip('0')
            
        if answer == "":
            return "0"
        return answer
            
obj = Solution()
ans = obj.removeKdigits("1432219",3)
print(ans)
