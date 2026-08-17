class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_num=set(nums)
        longest=0
        for num in unique_num:
            if num-1 not in unique_num:
                current=num
                len=1
                while current+1 in unique_num:
                    current+=1
                    len+=1
                longest=max(longest, len)
        return longest            

            
                