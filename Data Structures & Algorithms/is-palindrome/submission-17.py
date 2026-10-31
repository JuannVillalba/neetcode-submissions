class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1



        while l < r:
            while l < r and self.isalphanum(s[r]) == False: 
                l +=1 
            while r > l and self.isalphanum(s[r]) == False: 
                r -=1 
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True
    
    def isalphanum(self,c):
            return (ord(c) <= ord('z') and ord(c) >= ord('a')) or (ord(c) <= ord('Z') and ord(c) >= ord('A'))or (ord(c) <= ord('9') and ord(c) >= ord('0'))
            