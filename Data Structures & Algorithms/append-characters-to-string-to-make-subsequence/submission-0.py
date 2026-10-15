class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count = 0
        for ch in s:
            if count < len(t) and ch == t[count]:
                count += 1
        return len(t) - count            


        