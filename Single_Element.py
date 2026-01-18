class Solution:
    def singleNumber(self,num):
        result = 0
        for n in num:
            result = result ^ n
        return result

obj = Solution()
ans = obj.singleNumber([2,2,1,3,3,5,5,4,4])
print(ans)

