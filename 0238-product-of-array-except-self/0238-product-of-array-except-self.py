class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[1]*n

        left_side=1
        for i in range(n):
            result[i]=left_side
            left_side *= nums[i]

        right_side=1
        for i in range(n-1, -1, -1):
            result[i] *= right_side
            right_side *= nums[i]
        
        return result