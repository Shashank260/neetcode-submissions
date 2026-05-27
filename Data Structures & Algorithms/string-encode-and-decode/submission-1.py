class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        s=''
        if len(strs)==0:
            return s
        for x in strs:
            s+=str(len(x))+'#'+x 
        return s
    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            decoded.append(s[j+1:length+1+j])
            i=j+1+length
        return decoded    