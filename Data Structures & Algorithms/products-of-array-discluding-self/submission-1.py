class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        right = [1] * n
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        for j in range(n-2,-1,-1):
            right[j] = right[j+1] * nums[j+1]
            res[j] = right[j]*res[j]
        res[n-1] = right[n-1] * res[n-1] 
        return res