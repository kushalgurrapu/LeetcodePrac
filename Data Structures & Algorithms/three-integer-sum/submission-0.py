class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        sortednum = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and sortednum[i] == sortednum[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            target = -sortednum[i]
            while left < right:
                if sortednum[left] + sortednum[right] > target:
                    right -= 1
                elif sortednum[left] + sortednum[right] < target:
                    left += 1
                else:
                    answer.append([sortednum[i], sortednum[left], sortednum[right]])
                    left += 1
                    right -= 1
                    while left < right and sortednum[left] == sortednum[left - 1]:
                        left += 1
                    while left < right and sortednum[right] == sortednum[right + 1]:
                        right -= 1
        return answer