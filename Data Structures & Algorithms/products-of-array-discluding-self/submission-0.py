class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n_zero=0
        prod=1
        for i,num in enumerate(nums):
            if num==0:
                n_zero+=1
                ind=i
                if n_zero>1:
                    return [0]*len(nums)
            else:
                prod*=num
        if n_zero==1:
            l= [0]*len(nums)
            l[ind]=prod
            return l
        else:
            for i,num in enumerate(nums):
                nums[i]=int(prod/num)
            return nums
            