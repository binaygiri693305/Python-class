def twoSum(nums, target):
    num_map = {}
    index = 0
    while index < len(nums):
        res = target - nums[index]
        if res in num_map:
            return [num_map[res], index]
        num_map[nums[index]] = index
        index += 1
    return []

n = [2,7,11, 15]
print(twoSum(n,9))