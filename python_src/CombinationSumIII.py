class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.getCombination(result, [], k, n, 1)
        return result
    
    def getCombination(self,result, one_case, k, n, start):
        if 0 == k and n == 0:
            result.append(list(one_case))
            return
        
        for i in range(start,10):
            if i > n: return
            one_case.append(i)
            self.getCombination(result, one_case, k - 1, n - i, i + 1)
            del one_case[-1]
        
            