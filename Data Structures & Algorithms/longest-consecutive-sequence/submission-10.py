class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums=set(nums)
        longest=0
        for num in unique_nums:
            if num-1 not in unique_nums:
                current=num
                len=1
                while current+1 in unique_nums:
                    current+=1
                    len+=1
                longest=max(longest, len)
        return longest            
        