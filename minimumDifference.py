# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.

class Solution:
    def minimumDifference(self,num,k):
        num.sort()
        output = []

        for i in range(0,len(num)-k+1):
            diff = num[i+k-1]-num[i]

            output.append(diff)

        return min(output)
    
obj = Solution()
ans = obj.minimumDifference([1,2,3,4],2)
print(ans)
