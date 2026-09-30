class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=set()
        left=0
        max_len=0
        for index in range(len(s)):
            while s[index] in res:
                res.remove(s[left])
                left+=1
            res.add(s[index])
            max_len=max(max_len, index-left+1)
        return max_len        

        