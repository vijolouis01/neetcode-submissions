class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for index in range(len(strs[0])):
            ch=strs[0][index]
            for word in strs[1:]:
                if len(word) <= index or ch != word[index]:
                    return strs[0][: index]
        return strs[0]              
        