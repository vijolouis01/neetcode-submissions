class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=dict()
        for index in range(len(nums)):
            complement=target-nums[index]
            if complement in seen:
                return [seen[complement], index]
            seen[nums[index]]=index
                

                    