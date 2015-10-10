class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX = 0x7fffffff
        MIN = - MAX - 1
        positive = True
        if x < 0: 
            positive = False
            x = -x
        result = 0
        while x > 0:
            x,b = divmod(x,10)
            result = result * 10 + b
        if positive:
            if result > MAX:
                return 0
            else:
                return result
        else:
            result = -result
            if result < MIN:
                return 0
            else:
                return result
        