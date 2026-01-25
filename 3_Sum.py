class Solution:
    def threeSum(self, nums):
        output = set()
        
        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])
                if third in seen:
                    output.add(tuple(sorted([nums[i], nums[j], third])))
                seen.add(nums[j])
        
        return [list(t) for t in output]

obj = Solution()
ans = obj.threeSum([-1,0,1,2,-1,-4])
print(ans)