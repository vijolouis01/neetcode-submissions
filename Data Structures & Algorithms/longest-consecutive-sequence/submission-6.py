class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums=set(nums)
        longest=0
        for num in set_nums:
            if num-1 not in set_nums:
                current=num
                num=1
                while  current+1 in set_nums:
                    current +=1
                    num+=1
                longest=max(longest, num)
        return longest        


            
                