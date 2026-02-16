class Solution(object):
    def productExceptSelf(self, nums):
        s = 1
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = nums[i-1]*ans[i-1]
        for j in range(len(nums)-2, -1, -1):
            s *= nums[j+1]
            ans[j] *= s
        return ans