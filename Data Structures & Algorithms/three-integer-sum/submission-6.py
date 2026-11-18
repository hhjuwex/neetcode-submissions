class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []
        l = len(nums)
        for i in range(l-1):
            j,k = i+1,l-1
            target = -nums[i]
            while j < k:
                if nums[j]+nums[k] > target:
                    k -= 1
                elif nums[j]+nums[k] < target:
                    j += 1
                else:
                    if [nums[i],nums[j],nums[k]] not in res: res.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    j += 1

        return res