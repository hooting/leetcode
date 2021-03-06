class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = self.recursive(candidates, 0, target)
        for item in result:
            item.reverse()
        return result
    
    def recursive(self, candidates, index, target):
        if candidates[index] == target:
            return [[candidates[index]]]
        elif candidates[index] > target:
            return []
        else:
            result = []
            for i in range(index, len(candidates)):
                if target - candidates[i] == 0: 
                    result += [[candidates[i]]]
                    break
                ret = self.recursive(candidates, i, target - candidates[i])
            
                for item in ret:
                    item.append(candidates[i])
                result += ret
            return result
        