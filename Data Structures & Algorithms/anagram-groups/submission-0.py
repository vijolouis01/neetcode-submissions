class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_count=defaultdict(list)
        for word in strs:
            count=[0]*26
            for ch in word:
                count[ord(ch)-ord('a')] +=1
            dict_count[tuple(count)].append(word)
        return list(dict_count.values())        

        