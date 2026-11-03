#from collections import defaultDictionary
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #dic = dafaultDictionary(int)
        return not (len(nums) == len(set(nums)))
        