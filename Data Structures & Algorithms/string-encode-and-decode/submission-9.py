class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for word in strs:
            encoded+=f"{len(word)}#{word}"
        return encoded    
      
    def decode(self, s: str) -> List[str]:
        decoded=[]
        len_start=0
        while len_start<len(s):
            len_end=len_start
            while s[len_end] != "#":
                len_end+=1
            length=int(s[len_start: len_end])
            decoded.append(s[len_end+1:len_end+1+length])
            len_start=len_end+1+length
        return decoded    