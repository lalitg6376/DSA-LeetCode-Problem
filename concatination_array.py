class Solution:
    def findTheArrayConcVal(self,num):
        num.sort()

        i = 0
        j = len(num)-1
        output = []

        while i<j:
            concat = int(str(num[i])+str(num[j]))
            output.append(concat)
            i+=1
            j-=1
        if i==j:
            output.append(num[i])


        return sum(output)
    
obj = Solution()
ans = obj.findTheArrayConcVal([7,52,2,4])
print(ans)
