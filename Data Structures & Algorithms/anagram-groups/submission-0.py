class Solution:
    #Made this during first run, but you don't need it since you can make a "signature" key for a group of anagrams, being the frequency array, and just put the word in value of this key.
    def isAnagram(word1: str, word2: str) -> bool:
        if (len(word1) != len(word2)):
            return False
        count = [0] * 26
        for i in range(len(word1)):
            count[ord(word1[i]) - ord('a')] += 1
            count[ord(word2[i]) - ord('a')] -= 1
        return all(x == 0 for x in count)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        anagrams = {}
        for word in strs:
            freq = [0]*26
            for i in range(len(word)):
                freq[ord(word[i]) - ord('a')] += 1
            key = tuple(freq)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        return list(anagrams.values())

