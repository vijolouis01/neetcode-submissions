class Solution:
    def isValid(self, s: str) -> bool:
        pair={'}':'{', ']':'[', ')':'('}
        stack=[]
        for ch in s:
            if ch in pair:
                if len(stack) > 0 and pair[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0