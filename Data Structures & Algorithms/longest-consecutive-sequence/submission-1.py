class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res =0
        for x in set_nums:
            if x-1 not in set_nums:
                curr_res = 0
                while x+1 in set_nums:
                    curr_res += 1
                    x += 1
                res = max(res, curr_res+1)
        return res
        