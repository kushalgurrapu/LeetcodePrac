class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [1]*(n)
        left = 1
        right = 1
        for i in range(n):
            products[i] = products[i]*left
            products[n-i-1] = products[n-i-1]*right
            left = left * nums[i]
            right = right * nums[n-i-1]
        return products

