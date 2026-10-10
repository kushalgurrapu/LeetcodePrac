class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = set(['(', '[', '{'])
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if (not stack) or (stack[-1] == '(' and char != ')') or (stack[-1] == '[' and char != ']') or (stack[-1] == '{' and char != '}'):
                    return False
                stack.pop()
        return len(stack) == 0
