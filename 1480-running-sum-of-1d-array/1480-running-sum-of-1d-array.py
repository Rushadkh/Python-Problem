class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer=[]
        if len(nums)==0:
            return answer

        answer.append(nums[0])
        if len(nums)==1:
            return answer

        answer.append(nums[1]+nums[0])
        if len(nums)==2:
            return answer

        for i in range(2, len(nums)):
            answer.append(answer[i-1]+nums[i])
        return answer   