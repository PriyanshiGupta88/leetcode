class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        strs.sort()
        l=len(strs)
        if(l>0):
            a=strs[0]
            b=strs[l-1]
            l2=len(a)
            l3=len(b)
            i,j=0,0
            while(i<l2 and j<l3):
                if(a[i]!=b[j]):
                    break
                s=s+a[i]
                i+=1
                j+=1
            return s
        else:
            return ""
        
        
