class Solution {
public:

    string encode(vector<string>& strs) {
        string res;
        for(string word : strs) {
            int n = word.size();
            res += to_string(n) + '#' + word;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> decoded;
        int n = s.size();
        int i = 0;
        while(i < n) {
            string num;
            while (s[i] != '#') {
                num += s[i];
                i++;
            }
            //i is at '#' now.
            i++;
            int length = stoi(num);
            string word;
            while (length > 0 && i < n) {
                word += s[i];
                length--;
                i++;
            }
            decoded.push_back(word);
        }
        return decoded;
    }
};
