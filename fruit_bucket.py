class Solution:
    def totalFruit(self,num):
        Start = 0
        bucket = {}
        maxlen = 0

        for end in range(len(num)):
            if num[end] in bucket:
                bucket[num[end]]+=1
            else:
                bucket[num[end]]=1

            while len(bucket) > 2:
                bucket[num[Start]]-=1
                if bucket[num[Start]] == 0:
                    del bucket[num[Start]]
                Start+=1

            maxlen = max(maxlen,end-Start+1)
        return maxlen
    
obj = Solution()
ans = obj.totalFruit([1,2,1,2,3])
print(ans)
