class Solution:
    def reverse(self, x: int) -> int:
        n=0
        
        if(x<0):
            v=x*(-1)
        else:
            v=x*1
        while(v>0):
            d=v%10
            n=n*10+d
            v=v//10
        if((n<=(2**31)-1) and (n>=(-2)**31)):  
            if(x>0):
                return n
            else:
                return(n*(-1))
        else:
            return 0
