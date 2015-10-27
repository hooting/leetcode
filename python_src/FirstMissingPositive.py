class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        for i in range(size):
            pivot = nums[i]
            while 0 < pivot <= size and nums[pivot - 1] != pivot:
                nums[pivot - 1], pivot = pivot, nums[pivot - 1]
        for i in range(size):
            if nums[i] != i + 1: return i + 1
        return size + 1
        