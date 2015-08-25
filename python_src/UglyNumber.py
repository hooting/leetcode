class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        elif num <= 0: return False
        num = self.div(num,5)
        num = self.div(num,3)
        num = self.div(num,2)
        if num == 1: return True
        else: return False
    
    def div(self,num, divider):
        a = num / divider
        b = num % divider
        if b != 0: return num
        if a == 1: return 1
        else: return self.div(a,divider)
    
        