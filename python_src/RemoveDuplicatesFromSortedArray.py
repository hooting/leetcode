class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = 0
        for index,value in enumerate(nums):
            if index > 0 and nums[index - 1] == value: continue
            else: 
                nums[tail] = value
                tail += 1
        return tail
                
        