class Solution:
    def findMaxAverage(self,num,k):
        window_sum = sum(num[:k])
        max_sum = window_sum

        for i in range(k,len(num)):
            window_sum = window_sum-num[i-k]+num[i]
            if window_sum>max_sum:
                max_sum=window_sum

        return max_sum/k
    
obj = Solution()
ans = obj.findMaxAverage([1,2,3,4],3)
print(ans)
