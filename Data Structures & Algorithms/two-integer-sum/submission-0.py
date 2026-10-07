class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        
        for i in range(len(nums)):
            # freq[i] = nums[i]
            # if (complement in freq.values()):
            #     return []
            complement = target - nums[i]
            if (complement) in freq:
                return [freq.get(complement), i]
            freq[nums[i]] = i
        return False
