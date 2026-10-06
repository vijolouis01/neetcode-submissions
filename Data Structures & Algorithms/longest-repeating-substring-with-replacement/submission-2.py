class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = max_count = longest = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            max_count = max(max_count, count[ch])

            if right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest        