class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_positive = True
        if dividend < 0 and divisor < 0: 
            dividend = -dividend #may overflow, but in python, it's ok
            divisor = -divisor
        elif dividend > 0 and divisor < 0:
            divisor = -divisor
            is_positive = False
        elif dividend < 0 and divisor > 0:
            dividend = -dividend
            is_positive = False
        result = 0
        n = 0
        while dividend >= divisor:
            divisor <<= 1
            n += 1
        if n <= 0: return 0
        factor = 1
        for i in range(n):
            factor <<= 1
        
        while n >= 0:
            if dividend >= divisor:
                result += factor
                dividend -= divisor
            divisor >>= 1
            factor >>= 1
            n -= 1
        if not is_positive: result = -result
        if result > 0x7fffffff: return 0x7fffffff
        return result
            
            
            
        