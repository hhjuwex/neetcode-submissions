

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        try:
            for i in range(max(len(s),len(t))):
                if s[i] != t[i]: return False
        except:
            return False
        return True
        
        