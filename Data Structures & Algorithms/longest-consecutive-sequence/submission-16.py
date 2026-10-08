class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                current = num
                current_length = 1
                while current + 1 in nums:
                    current += 1
                    current_length += 1
                if longest < current_length:
                    longest = current_length
        return longest                        