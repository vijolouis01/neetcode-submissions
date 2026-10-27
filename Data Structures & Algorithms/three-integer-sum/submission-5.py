class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index in range(len(nums) - 2):
            left = index + 1
            right = len(nums) - 1
            if nums[index] > 0:
                break
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            while left < right:
                total = nums[index] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result                    

        