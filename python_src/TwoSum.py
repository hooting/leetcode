class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #if there are two same values in nums, the last one will cover the first one, 
        #in the for loop, as iterate from the begin to the end, we can fetch both of these two index
        d = {value:index for index,value in enumerate(nums)}
        index1 = index2 = 1
        for i,value in enumerate(nums):
            if target - value in d:
                index1 += i
                index2 += d[target-value]
                if target - value == value and index1 == index2:
                    continue
                else:
                    break
        if index1 > index2:
            index1, index2 = index2, index1
        return [index1,index2]
        
        