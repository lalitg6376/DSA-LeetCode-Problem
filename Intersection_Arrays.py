class Solution:
    def intersection(self,num1,num2):
        result = []
        for i in range(len(num1)):
            for j in range(len(num2)):
                if num1[i] == num2[j]:
                    if num1[i] not in result:
                        result.append(num1[i])
        return result
                    
obj = Solution()
ans = obj.intersection([1,2,3,4],[1,5,2,6])

print(ans)