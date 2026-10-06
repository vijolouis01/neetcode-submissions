class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0]*26
        max_freq = left = max_window = 0
        for right in range(len(s)):

            freq[ord(s[right]) - ord('A')] += 1

            max_freq = max(max_freq, freq[ord(s[right]) - ord('A')])

            window_len = right - left + 1

            if window_len - max_freq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            window_len = right - left + 1 
            max_window = max(max_window, window_len)
        return max_window

        