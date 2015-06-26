class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        lenN = len(nums);
        if lenN == 0:
            return []
        first, last = 0,1
        result = []
        while last < lenN:
            if (nums[last] - nums[last - 1] != 1):
                if last - first == 1:
                    result.append(str(nums[first]))
                else:
                    result.append(str(nums[first]) + "->" + str(nums[last - 1]))
                first = last
            last += 1
        if last - first == 1:
            result.append(str(nums[first]))
        else:
            result.append(str(nums[first]) + "->" + str(nums[last - 1]))
        return result
            