class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> seen;
        for(int num : nums) {
            seen.insert(num);
        }
        unordered_map<int, int> thing;
        for(int num : nums) {
            if (!seen.count(num-1)) {
                thing[num] = 1;
            }
        }
        int mx = 0;
        for(auto& [key, val] : thing) {
            int num = key+1;
            while (seen.count(num)) {
                thing[key]++;
                num++;
            }
            mx = max(mx, thing[key]);
        }
        return mx;
    }
};
