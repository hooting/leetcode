class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n < 0: 
            x = 1 / x
            n = -n
        if n % 2 == 0: return self.myPositivePow(x * x, n / 2)
        else: return x * self.myPositivePow(x * x, n / 2)
    
    def myPositivePow(self,x,n):
        if n == 0: return 1
        if n % 2 == 0: return self.myPositivePow(x * x, n / 2)
        else: return x * self.myPositivePow(x * x, n / 2)
        