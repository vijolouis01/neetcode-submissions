class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[1]*len(nums)
        pre_fix=1
        for index in range(len(nums)):
            product[index]=pre_fix
            pre_fix*=nums[index]
        post_fix=1    
        for index in range(len(nums)-1, -1, -1):
            product[index]*=post_fix   
            post_fix*=nums[index] 
        return product    
            

        