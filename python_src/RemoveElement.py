class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        available = 0
        for index, value in enumerate(nums):
            if value == val: continue
            else:
                nums[available] = value
                available += 1
        return available