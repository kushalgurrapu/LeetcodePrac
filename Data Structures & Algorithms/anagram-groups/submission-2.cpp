class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        map<array<int, 26>, vector<string>> groups;
        for(string word : strs) {
            array<int, 26> freq{};
            for(char letter : word) {
                freq[(int)letter - (int)'a']++;
            }
            groups[freq].push_back(word);
        }
        for (auto [key, val] : groups) {
            res.push_back(val);
        }
        return res;
    }
};
