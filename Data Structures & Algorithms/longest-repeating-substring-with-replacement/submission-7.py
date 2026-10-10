class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxLength = 0
        left = 0
        mostFreq = 0
        for right, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1
            mostFreq = max(mostFreq, freq[char])
            if (right - left + 1) - k > mostFreq:
                freq[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength
            