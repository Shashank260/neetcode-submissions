class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i,num in enumerate(nums):
            comp=target - nums[i]
            if comp in s:
                return sorted([i, s[comp]])
            s[nums[i]]=i
