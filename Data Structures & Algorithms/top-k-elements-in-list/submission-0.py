class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=defaultdict(int)
        for x in nums:
            s[x]+=1
        l=sorted(s, key=lambda x:s[x], reverse=True)
        return l[0:k]
