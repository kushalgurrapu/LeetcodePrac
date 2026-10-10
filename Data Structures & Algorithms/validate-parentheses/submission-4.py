class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        stack = []
        for char in s:
            if char in paren:
                stack.append(char)
            elif stack and paren[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack