class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters=re.sub(r'[^a-zA-Z0-9]',"", s).lower()
        print(letters)
        return letters.lower() == letters[::-1].lower()
        