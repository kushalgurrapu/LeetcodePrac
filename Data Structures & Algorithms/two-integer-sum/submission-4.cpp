class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indexes;
        for(int i = 0; i < nums.size(); i++) {
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
