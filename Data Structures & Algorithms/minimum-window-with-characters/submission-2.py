class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freqT = {}
        distinct = 0
        for char in t:
            if char not in freqT:
                freqT[char] = 1
                distinct += 1
            else:
                freqT[char] += 1
        freqS = {}
        left = 0
        have = 0
        minlength = len(s)+1
        minleft = 0
        minright = 0
        for right, char in enumerate(s):
            if char in freqT:
                freqS[char] = freqS.get(char, 0) + 1
                if freqS[char] == freqT[char]:
                    have += 1
            while have == distinct:
                if minlength > right - left + 1:
                    minlength = right - left + 1
                    minleft = left
                    minright = right
                if s[left] in freqT:
                    freqS[s[left]] -= 1
                    if freqS[s[left]] < freqT[s[left]]:
                        have -= 1
                left += 1
        if minlength == len(s) + 1:
            return ""
        return s[minleft: minright + 1]


        