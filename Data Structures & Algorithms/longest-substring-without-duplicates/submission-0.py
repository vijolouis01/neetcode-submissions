class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_set=set()
        l=0
        max_len=0
        for index in range(len(s)):
            while s[index] in res_set:
                res_set.remove(s[l])
                l+=1
            res_set.add(s[index])
            max_len=max(max_len, index-l+1)
        return max_len    
        

        