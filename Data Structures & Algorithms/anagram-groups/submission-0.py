class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s=defaultdict(list)
        for x in strs:
            s[tuple(sorted(x))].append(x)
        l=[]
        for x in s:
            l.append(s[x])
        return l
