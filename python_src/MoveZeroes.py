class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        insert_pos = 0
        pivot = 0
        while(pivot < size):
            if nums[pivot] != 0:
                nums[insert_pos] = nums[pivot]
                insert_pos += 1
            pivot += 1
        while(insert_pos < size):
            nums[insert_pos] = 0
            insert_pos += 1
            