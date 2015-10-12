class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numToChar = dict()
        numToChar['2'] = ['a','b','c']
        numToChar['3'] = ['d','e','f']
        numToChar['4'] = ['g','h','i']
        numToChar['5'] = ['j','k','l']
        numToChar['6'] = ['m','n','o']
        numToChar['7'] = ['p','q','r','s']
        numToChar['8'] = ['t','u','v']
        numToChar['9'] = ['w','x','y','z']
        if len(digits) == 0: return []
        result = [[x] for x in numToChar[digits[0]]]
        digits = digits[1:]
        for c in digits:
            temp = []
            for lst in result:
                for item in numToChar[c]:
                    newOne = list(lst)
                    newOne.append(item)
                    temp.append(newOne)
            result = temp
        result = ["".join(x) for x in result]
        return result