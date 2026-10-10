class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        start = 0
        maxfreq = 0
        length = 0
        maxlength = 0
        for i, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1
            maxfreq = max(freq[char], maxfreq)
            length += 1
            if maxfreq < length - k:
                freq[s[start]] -= 1
                start += 1
                length -= 1
            maxlength = max(maxlength, length)
        return maxlength


