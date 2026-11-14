class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> seen(nums.begin(), nums.end());

        int mx = 0;

        for (int num : seen) {
            if (!seen.count(num - 1)) {
                int len = 1;
                int curr = num;

                while (seen.count(curr + 1)) {
                    curr++;
                    len++;
                }

                mx = max(mx, len);
            }
        }

        return mx;
    }
};