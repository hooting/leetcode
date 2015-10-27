class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        size1 = len(num1)
        size2 = len(num2)
        
        num1 = [int(x) for x in num1]
        num2 = [int(x) for x in num2]
        num1.reverse()
        num2.reverse()
        result = [0] * (size1 + size2)
        for i in range(size1):
            for j in range(size2):
                temp = num1[i] * num2[j]
                result[i + j + 1] += temp / 10
                result[i + j] += temp % 10
        for i, value in enumerate(result):
            try:
                result[i + 1] += value / 10
                result[i] = value % 10
            except:
                pass
        while len(result) > 1 and result[-1] == 0: del result[-1]
        result.reverse()
        return "".join([str(x) for x in result])
        
        