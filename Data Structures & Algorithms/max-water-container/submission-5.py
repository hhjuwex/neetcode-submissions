class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = len(heights)
        i = 0
        j = l-1
        while i < j:
            res = max(res,(j-i) * min(heights[i],heights[j]))
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return res