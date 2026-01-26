# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
        def sortedSquares(self,num):
            n = len(num)
            output = [0]*n
            i = 0
            j = n-1
            for k in range(n-1,-1,-1):
                if num[i] * num[i] > num[j]* num[j]:
                    output[k] = num[i] * num[i]
                    i+=1
                else:
                    output[k] = num[j] * num[j]
                    j-=1
            return output
        
obj = Solution()
ans = obj.sortedSquares([1,2,3,4])
print(ans)
