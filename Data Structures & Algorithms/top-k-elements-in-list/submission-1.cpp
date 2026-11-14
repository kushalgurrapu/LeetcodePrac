class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res(k);
        unordered_map<int, int> freq;
        int n = nums.size();
        priority_queue<pair<int, int>> q;
        for(int i = 0; i < n; i++) {
            freq[nums[i]]++;
        }
        for(auto [key, val] : freq) {
            q.push({val, key});
        }
        int i = 0;
        while (!q.empty() && i < k) {
            res[i] = q.top().second;
            q.pop();
            i++;
        }
        return res;
    }
};
