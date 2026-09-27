class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 !=0:
            return False 
        stack=[]
        pair={'}':'{', ']':'[', ')':'('}
        for ch in s:
            if ch in "[{(":
                stack.append(ch)
            else:
                if not stack or stack[-1] != pair[ch]:
                    return False  
                stack.pop()
        return not stack             


        