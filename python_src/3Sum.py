class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        size = len(nums)
        for i in range(size - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            start = i + 1
            end = size - 1
            while start < end:
                sum = nums[start] + nums[end] + nums[i]
                if sum == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]: start += 1
                    while end > start and nums[end] == nums[end+1]: end -= 1
                elif sum > 0:
                    end -= 1
                else:
                    start += 1
        return result
            