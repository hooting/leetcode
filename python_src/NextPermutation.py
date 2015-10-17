class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for i in range(size - 1, -1, -1):
            min = 0x7fffffff
            index = -1
            for j in range(size-1,i-1,-1):
                if nums[i] < nums[j]:
                    if min > nums[j]:
                        min = nums[j]
                        index = j
            if index != -1:
                nums[i],nums[index] = nums[index],nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                return
        return nums.sort()