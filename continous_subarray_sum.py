# continous subarray sum

class Solution:
    def checkSubarraySum(self,num,k):
        remainder_map = {0:-1}
        sum = 0
        for i in range(len(num)):
            sum+=num[i]
            remainder = sum%k

            if remainder in remainder_map:
                if i-remainder_map[remainder]>=2:
                    return True
            else:
                remainder_map[remainder]=i
                
        return False
    
obj = Solution()
ans = obj.checkSubarraySum([5,0,0,0],3)
print(ans)
