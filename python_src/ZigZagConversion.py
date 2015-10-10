class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lines = [[] for i in range(numRows)]
        lineIndex = 0
        down = True
        for c in s:
            lines[lineIndex].append(c)
            if down:
                if lineIndex < numRows - 1:
                    lineIndex += 1
                else:
                    down = False
                    lineIndex -= 1
            else:
                if lineIndex > 0:
                    lineIndex -= 1
                else:
                    down = True
                    lineIndex += 1
        lines = ["".join(line) for line in lines]
        return "".join(lines)