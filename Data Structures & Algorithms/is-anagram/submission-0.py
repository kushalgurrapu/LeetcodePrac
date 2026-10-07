class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        freqS = {}
        freqT = {}
        commonlen = len(s)
        for n in range(0, commonlen):
            freqS[s[n]] = freqS.get(s[n], 0) + 1
            freqT[t[n]] = freqT.get(t[n], 0) + 1
        return (freqS == freqT)
