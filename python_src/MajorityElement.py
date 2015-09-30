class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = count = 0
        for item in nums:
            if count == 0:
                majority = item
                count = 1
            elif item == majority:
                count += 1
            else:
                count -= 1
        return majority