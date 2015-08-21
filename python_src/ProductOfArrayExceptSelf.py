class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        zero_num = 0
        zero_index = -1
        for i in nums:
            if i == 0: 
                zero_num += 1
                zero_index = nums.index(i)
            else: product *= i
        if zero_num > 1: return [0] * len(nums)
        elif zero_num == 1:
            output = [0] * len(nums)
            output[zero_index] = product
        else:
            output = [product / i for i in nums]
        return output
        