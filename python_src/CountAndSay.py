class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = [1]
        for i in range(n - 1):
            temp = []
            num = 1
            for index, value in enumerate(result):
                try:
                    if result[index] == result[index + 1]: num += 1
                    else: 
                        temp.append(num)
                        temp.append(value)
                        num = 1
                except IndexError:
                    temp.append(num)
                    temp.append(value)
            result = temp
        return "".join([str(x) for x in result])