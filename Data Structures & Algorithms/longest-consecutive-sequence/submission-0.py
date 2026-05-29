class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        for num in nums:
          s.add(num)
        l=0
        for num in nums:
            if num-1 not in s:
                lt=0
                while num+lt in s:
                    lt+=1
                l=max(l,lt)
        return l