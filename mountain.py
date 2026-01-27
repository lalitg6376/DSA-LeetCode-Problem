#Valid mountain array

class Solution:
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False
        
        peak = -1
        
        # increasing part
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                peak = i
            else:
                break
        
        # peak first ya last nahi ho sakta
        if peak == -1 or peak == n-1:
            return False
        
        # decreasing part
        for i in range(peak+1, n):
            if arr[i] >= arr[i-1]:
                return False
        
        return True


obj = Solution()
print(obj.validMountainArray([2, 0, 2]))     # False
print(obj.validMountainArray([0, 3, 2, 1]))  # True
