class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram=defaultdict(list) 
        for word in strs:
            count=[0]*26
            for ch in word:
                count[ord(ch)-ord('a')]+=1
            group_anagram[tuple(count)].append(word)
        return list(group_anagram.values())        



        