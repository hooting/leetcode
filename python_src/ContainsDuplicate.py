class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        to_set = set(nums)
        return not len(to_set) == len(nums)
        