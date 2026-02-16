class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums

        
obj = Solution()
nums = [2, 0, 2, 1, 1, 1]
# nums = [2, 0, 1]
r = obj.sortColors(nums)
print(r)