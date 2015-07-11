class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        result = []
        one = []
        self.recursiveCombine(n,k,1,result,one)
        return result
    
    def recursiveCombine(self, n, k, start, result, one):
        if k == 0:
            result.append(list(one))
            return
        for i in range(start, n - k + 2):
            one.append(i)
            self.recursiveCombine(n,k-1,i + 1,result,one)
            one.pop()
        
        