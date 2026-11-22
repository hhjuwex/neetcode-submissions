class Solution:
    def trap(self, height: list[int]) -> int:
        res1 = 0
        l1 = len(height)
        
        l = 0
        r = l1 - 1
        lmax = rmax = 0

        while l < r:
            if height[l] < height[r]:
                lmax = max(height[l],lmax)
                res1 += lmax - height[l]
                l += 1
            else:
                rmax = max(height[r],rmax)
                res1 += rmax - height[r]
                r -= 1
            
        return res1