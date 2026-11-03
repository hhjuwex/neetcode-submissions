class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)).zfill(3) + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            len_s = int(s[i:i+3])
            res.append(s[i+3:i+3+len_s])
            i += 3 + len_s
        return res
