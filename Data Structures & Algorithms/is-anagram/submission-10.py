class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        t_count, s_count=dict(), dict()
        for index in range(len(s)):
            s_count[s[index]]=s_count.get(s[index], 0)+1
            t_count[t[index]]=t_count.get(t[index], 0)+1
        return s_count==t_count    
