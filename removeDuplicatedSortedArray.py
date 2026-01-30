class Solution:
    def removeDuplicates(self, nums):
        c = 0
        for i in range(1, len(nums)):
            if nums[c] != nums[i]:
                count += 1
                nums[c] = nums[i]
        return c+1
            