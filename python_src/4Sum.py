class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        size = len(nums)
        result = []
        for i in range(size - 3):
            if nums[i] * 4 > target: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            target3 = target - nums[i]
            for j in range(i+1, size - 2):
                if nums[j] * 3 > target3: break
                if j > i+1 and nums[j] == nums[j-1]: continue
                target2 = target3 - nums[j]
                start = j + 1
                end = size - 1
                while start < end:
                    if nums[start] * 2 > target2 or nums[end] * 2 < target2: break
                    temp = nums[start] + nums[end]
                    if temp == target2:
                        result.append([nums[i],nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start-1]: start += 1
                        while end > start and nums[end] == nums[end+1]: end -= 1
                    elif temp > target2:
                        end -= 1
                    else:
                        start += 1
        return result
                
    
    