class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in range(len(tokens)):

            if stack and tokens[i] == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 + val2)
            elif stack and tokens[i] == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif stack and tokens[i] == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 * val2)
            elif stack and tokens[i] == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]


        