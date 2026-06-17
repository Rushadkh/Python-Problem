class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        new_list=set(nums)
        if len(new_list)>2:
            new_list.remove(max(new_list))
            new_list.remove(max(new_list))
            return max(new_list)
        else:
            return max(new_list)