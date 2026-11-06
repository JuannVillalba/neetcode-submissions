class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s) -1
        while l < r:
            while s[l].isalpha() == False and l < r:
                l +=1 
            while s[r].isalpha() == False and r > l:
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1
        return True

    def isalpha(self, c):
        return ( ord('a') <= ord(c) <= ord('z')
                or ord('A') <= ord(c) <= ord('Z')
                or ord('0') <= ord(c) <= ord('9'))

