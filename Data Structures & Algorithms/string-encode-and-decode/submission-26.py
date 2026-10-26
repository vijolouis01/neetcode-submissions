class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded    


    def decode(self, s: str) -> List[str]:
        len_start = 0
        decoded = []
        while len_start < len(s):
            len_end = len_start
            while s[len_end] != "#":
                len_end += 1
            length = int(s[len_start : len_end])
            len_start = len_end + 1
            decoded.append(s[len_start : len_start + length])
            len_start = len_end + length + 1
        return decoded    


