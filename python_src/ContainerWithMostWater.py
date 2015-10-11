"""
reference to https://leetcode.com/discuss/1074/anyone-who-has-a-o-n-algorithm
explaination can also be seen in https://leetcode.com/discuss/11482/yet-another-way-to-see-what-happens-in-the-o-n-algorithm
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        result = 0
        while(start < end):
            result = max(result,(end - start) * min(height[start],height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return result