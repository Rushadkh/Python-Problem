class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water=0
        left=0
        right=len(height)-1

        while left < right:
            l=right-left 
            h=min(height[left], height[right])

            current=l*h

            max_water=max(max_water, current)

            if height[right]>height[left]:
                left += 1
            else:
                right -= 1
        return max_water        