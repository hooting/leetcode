#reference to:
#https://leetcode.com/discuss/42806/boyer-moore-majority-vote-algorithm-generalization

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        x,y = 0,1
        cx = cy = 0
        for i in nums:
            if x == i: cx += 1
            elif y == i: cy += 1
            elif cx == 0: 
                cx = 1
                x = i
            elif cy == 0:
                cy = 1
                y = i
            else:
                cx -= 1
                cy -= 1
        cx = cy = 0
        for i in nums:
            if x == i:
                cx += 1
            elif y == i:
                cy += 1
        result = []
        if cx > len(nums) / 3:
            result.append(x)
        if cy > len(nums) / 3:
            result.append(y)
        return result
        