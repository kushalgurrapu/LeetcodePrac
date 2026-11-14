class Solution {
public:
    bool isAnagram(string s, string t) {
        int s_size = s.size();
        int t_size = t.size();
        if (s_size != t_size) {
            return false;
        }
        unordered_map<char, int> freq;
        for(int i = 0; i < s_size; i++) {
            freq[s[i]]++;
            freq[t[i]]--;
        }
        for(auto [key, val] : freq) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
};
