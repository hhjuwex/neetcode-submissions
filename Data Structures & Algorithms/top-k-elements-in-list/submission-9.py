class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cnt = Counter(nums)
        res = [[] for _ in range(n+1)]
        for i in cnt:
            res[cnt[i]].append(i)
        #return [res[i] for i in range(n, 0, -1) if res[i]]
        return [item for jtem in range(n, 0, -1) for item in res[jtem]][:k]
        