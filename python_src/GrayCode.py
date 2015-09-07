class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [0]
        for i in range(n):
            temp = list(ret)
            cur = 1 << i
            for j in reversed(temp):
                ret.append(j + cur)
        return ret
            