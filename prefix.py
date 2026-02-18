#prefix sum

arr = [2,4,1,6,3]

prefix = [0]*len(arr)
print(prefix)
prefix[0] = arr[0]
for i in range(1,len(arr)):
     prefix[i]=prefix[i-1]+arr[1]
print(prefix)
