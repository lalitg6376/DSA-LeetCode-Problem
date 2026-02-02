class Solution:
    def threeSumClosest(self,num,tar):
        num.sort()
        fix = 0
        n = len(num)
         
        best = num[0]+num[1]+num[2]
        for fix in range(n-2):
            i = fix+1
            j =  n-1
            while i< j:
                curr = num[fix]+num[i]+num[j]
                if abs(curr-tar) < abs(best-tar):
                    best =  curr
                if curr < tar:
                    i+=1
                else:
                    j-=1
        return best
obj = Solution()
ans = obj.threeSumClosest([-1,2,1,-4],1)
print(ans)