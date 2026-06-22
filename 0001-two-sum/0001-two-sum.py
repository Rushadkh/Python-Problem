class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}

        for i in range(len(nums)):
            curr = target-nums[i]

            if curr in dic:
                return [dic[curr], i]
            
            dic[nums[i]] = i