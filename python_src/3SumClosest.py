class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        distance = 0x7fffffff
        result = 0
        size = len(nums)
        for i in range(size - 2):
            start = i + 1
            end = size - 1
            while start < end:
                sum = nums[start] + nums[end] + nums[i]
                temp = sum - target
                if abs(temp) < distance:
                    distance = abs(temp)
                    result = sum
                if temp == 0:
                    return sum
                elif temp > 0:
                    end -= 1
                else:
                    start += 1
        return result