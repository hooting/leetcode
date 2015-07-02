class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        results = []
        size = len(nums)
        if size == 0: return 0
        elif size <= 2: return max(nums)
        results.append(nums[0])
        results.append(nums[1])
        results.append(nums[0] + nums[2])
        for i in range(3,size):
            results.append(max(nums[i] + results[i - 2], nums[i] + results[i - 3]))
        return max(results)
        