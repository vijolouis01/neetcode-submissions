class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count1 = [0]*26
        count2 = [0]*26
        for index in range(len(s)):
            count1[ord(s[index]) - ord('a')] += 1
            count2[ord(t[index]) - ord('a')] += 1
        return count1 == count2    

