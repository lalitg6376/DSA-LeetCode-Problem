class solution:
    def find(self,c):
        

        i = 0
        j = int(c**0.5)
        while i<=j:
            s = i*i+j*j
            if s==c:
                return True
            elif s<c:
                i+=1
            else:
                j-=1
            
        
        return False
            
obj = solution()
ans = obj.find(5)
print(ans)
