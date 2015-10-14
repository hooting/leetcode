class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.addPar('',n,0)
        return self.result
    
    def addPar(self, subStr, leftNum, rightNum):
        if leftNum == rightNum == 0:
            self.result.append(subStr)
        
        if leftNum > 0:
            self.addPar(subStr + '(', leftNum - 1, rightNum + 1)
        if rightNum > 0: 
            self.addPar(subStr + ')',leftNum, rightNum - 1)
            
        