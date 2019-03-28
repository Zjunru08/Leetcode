class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        size = len(x)
        
        for i in range((size+1)//2):
            if x[i] == x[size-1-i]:
                pass
            else:
                return False
        
        return True
