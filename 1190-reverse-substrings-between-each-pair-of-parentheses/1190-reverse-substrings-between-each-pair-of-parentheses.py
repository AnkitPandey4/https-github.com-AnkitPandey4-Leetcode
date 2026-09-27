class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  # Remove '('
                stack.extend(temp)  # Append reversed chars back
            else:
                stack.append(char)
        return "".join(stack)
