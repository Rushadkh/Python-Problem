class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
                       
            while left < right:
                a = nums[left] + nums[right] + nums[i]
                if a>0:
                    right -= 1
                elif a<0:
                    left += 1
                elif a==0:
                    result.append([nums[left], nums[right], nums[i]])
                    while left < right and nums[left]==nums[left+1]:
                        left += 1
                    while left < right and nums[right]==nums[right-1]:
                        right -= 1

                    left += 1
                    right -+ 1
                    
                
        return result
