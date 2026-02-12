class Solution:
    def numSubarrayProductLessThanK(self,num,k):
        if k<=1:
            return 0
        
        start = 0
        count = 0
        product = 1

        for end in range(len(num)):
            product*=num[end]
            
            while product >= k:
                product//=num[start]
                start+=1
            count+=(end-start+1)
        return count


obj = Solution()
ans = obj.numSubarrayProductLessThanK([10,5,2,6],100)
print(ans)

