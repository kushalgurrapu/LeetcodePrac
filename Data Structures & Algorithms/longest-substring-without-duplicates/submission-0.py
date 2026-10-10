class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastseen = {}
        maxlength = 0
        start = 0
        length = 0
        for i, char in enumerate(s):
            if char in lastseen and lastseen[char] >= start:
                start = lastseen[char] + 1
                length = i - start
            lastseen[char] = i
            length += 1
            maxlength = max(maxlength, length)
        return maxlength

            