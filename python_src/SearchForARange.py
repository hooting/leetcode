class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        index = self.searchIndex(nums, target, 0, end)
        if index == -1: return [-1,-1]
        leftIndex = rightIndex = index
        while True:
            temp = self.searchIndex(nums, target, 0, leftIndex - 1)
            if temp == -1: break
            else: leftIndex = temp
        while True:
            temp = self.searchIndex(nums, target, rightIndex + 1, end)
            if temp == -1: break
            else: rightIndex = temp
        return [leftIndex, rightIndex]
        
    def searchIndex(self, nums, target, start, end):
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: end = mid - 1
            else: start = mid + 1
        return -1