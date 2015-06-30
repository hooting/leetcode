class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        result = []
        oneCase = []
        nums.sort()
        self.recurPermute(result,nums,oneCase)
        return result
    
    # @param {integer[][]} result
    # @param {integer[]} nums
    # @param {integer[]} oneCase
    def recurPermute(self,result,nums,oneCase):
        if len(nums) == 0: 
            result.append(list(oneCase))
            return
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            oneCase.append(nums[i])
            rest = list(nums)
            del rest[i]
            self.recurPermute(result,rest,oneCase)
            oneCase.pop()
            
            