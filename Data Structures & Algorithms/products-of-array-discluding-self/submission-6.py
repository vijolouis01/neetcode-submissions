class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[1]*len(nums)
        pre=1
        for index in range(len(nums)):
            product[index]=pre
            pre*=nums[index]
        post=1
        for index in range(len(nums)-1, -1, -1):
            product[index]*=post
            post*=nums[index]
        return product         


        