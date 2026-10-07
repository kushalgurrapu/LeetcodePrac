class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + '#' + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            strLength = ""
            while s[i] != '#':
                strLength += s[i]
                i += 1
            intLength = int(strLength)
            word = ""
            while intLength > 0:
                word += s[i+1]
                i += 1
                intLength -= 1
            decoded.append(word)
            i += 1
        return decoded