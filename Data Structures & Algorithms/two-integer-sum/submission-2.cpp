class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        unordered_map<int, int> indexes;
        for(int i = 0; i < nums.size(); i++) {
            // if (!indexes.count(nums[i])) {
            //     indexes[nums[i]] = i;
            // }
            int complement = target - nums[i];
            if (indexes.count(complement)) {
                if (indexes[complement] != i) {
                    return {indexes[complement], i};
                }
            }
            indexes[nums[i]] = i;
        }
    }
};
