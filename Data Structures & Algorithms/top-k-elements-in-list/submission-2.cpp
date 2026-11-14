class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> res;
        vector<vector<int>> buckets(n);
        unordered_map<int, int> freq;
        for(int num : nums) {
            freq[num]++;
        }
        for (auto [key, val] : freq) {
            buckets[val-1].push_back(key);
        }
        for(int i = n-1; i >= 0; i--) {
            for(int num : buckets[i]) {
                if (res.size() == k) {
                    return res;
                }
                res.push_back(num);
            }
        }
        return res;
    }
};
