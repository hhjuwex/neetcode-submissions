class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [i[0] for i in sorted(c.items(), reverse = True, key = lambda item: item[1])[:k]]
        