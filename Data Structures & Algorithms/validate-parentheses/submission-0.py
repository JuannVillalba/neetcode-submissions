class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {')':'(', '}':'{', ']': '['}
        stack = []

        for c in s:

            if stack and c in myMap:
                if myMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

            