class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        count = [0] * 26
        for n in range(0, len(s)):
            count[ord(s[n]) - ord('a')] += 1
            count[ord(t[n]) - ord('a')] -= 1
        for x in count:
            if x != 0:
                return False
        return True
