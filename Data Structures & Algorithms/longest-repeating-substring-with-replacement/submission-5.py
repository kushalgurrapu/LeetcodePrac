class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mostFreq = 0
        freq = {}
        left = 0
        right = 0
        maxlength = 0
        length = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            mostFreq = max(mostFreq, freq[s[right]])
            length = right - left + 1
            if length - mostFreq > k:  
                freq[s[left]] -= 1
                left += 1
                length -=1
            right += 1
            maxlength = max(maxlength, length)
        return maxlength
            