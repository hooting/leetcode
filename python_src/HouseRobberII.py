class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        size = len(nums)
        if size == 0: return 0
        elif size == 1: return nums[0]
        nums1 = nums[0: size - 1]
        max1 = self.noNeighbor(nums1)
        nums2 = nums[1:]
        max2 = self.noNeighbor(nums2)
        return max(max1,max2)
        
    def noNeighbor(self, nums):
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
        
        