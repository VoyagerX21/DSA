class Solution:
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr = sorted(set(arr))
        for i in range(len(arr)):
            if arr[i] >= 1:
                break
        
        j = 1
        while i < len(arr):
            if arr[i] != j:
                return j
            else:
                i+=1
                j+=1
            
        return j

obj = Solution()
ln = [[5, 3, 2, 5, 1], [-8, 0, -1, -4, -3], [1,2,3,4,5]]

for i in ln:
    print(obj.missingNumber(i))