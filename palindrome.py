class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=0
        num=x
        if(x>=0):
            while(x>0):
                n=(n*10)+x%10
                x=x//10
            if(num==n):
                return True
            else:
                return False
        else:
            return False
        
