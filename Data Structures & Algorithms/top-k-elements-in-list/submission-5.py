class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        lt = sorted(c.items(), reverse = True, key = lambda item: item[1])
        return [lt[i][0] for i in range(len(lt)) if i < k]
        