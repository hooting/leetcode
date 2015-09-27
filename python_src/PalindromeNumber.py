class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed = 0
        back = x
        while x > 0:
            reversed = reversed * 10 + x % 10
            x /= 10
        if back == reversed:
            return True
        else:
            return False
        