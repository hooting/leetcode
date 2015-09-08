# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while(start <= end):
            pivot = (start + end) / 2
            if isBadVersion(pivot):
                if pivot == 1:
                    return 1
                else:
                    if not isBadVersion(pivot -1): return pivot
                end = pivot - 1
            else:
                start = pivot + 1
        return pivot