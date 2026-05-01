class Solution:
    def isValid(self, s: str) -> bool:

        valid = { ']' : '[' , '}' : '{' , ')' : '('}
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{': 
                stack.append(c)

            else :
                if stack and stack [-1] == valid[c]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False

  

            