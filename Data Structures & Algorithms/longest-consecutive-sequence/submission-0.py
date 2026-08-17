class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums=set(nums)
        longest=0
        for index in range(len(nums)):
            num=nums[index]
            if num-1 in set_nums:
                continue
            length=0    
            while num in set_nums:
                length+=1
                num+=1
            longest=max(longest, length)
        return longest    




        