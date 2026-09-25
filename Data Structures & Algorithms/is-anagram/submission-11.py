class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch_count=dict()
        for ch in s:
            ch_count[ch]=ch_count.get(ch, 0)+1
        for ch in t:
            if ch not in ch_count:
                return False
            ch_count[ch] -= 1
            if ch_count[ch] == 0:
                del ch_count[ch]
        return not ch_count                
        