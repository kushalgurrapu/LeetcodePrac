class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = {}
        distinct = 0
        minlength = len(s) + 1
        for char in t:
            if char in need:
                need[char] += 1
            else:
                need[char] = 1
                distinct += 1
        left = 0
        right = 0
        window = {}
        have = 0
        minleft = 0
        minright = 0
        while right < len(s):
            if s[right] in need:
                window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in need and need[s[right]] == window[s[right]]:
                have += 1
            right += 1
            while have == distinct:
                length = right - left
                if minlength > length:
                    minlength = length
                    minleft = left
                    minright = right
                if s[left] in window:
                    if window[s[left]] == need[s[left]]:
                        have -= 1
                    window[s[left]] -= 1
                left += 1
        return s[minleft:minright]
                    
                

            

