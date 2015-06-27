#add each matched tuple (leftIndex, rightIndex) to indexes
#sort indexes by leftIndex
#if rightIndex1 > leftIndex2 then the latter is capsuled by the former one
#elif rightIndex1 + 1 = leftIndex2 then they are adjecent
#else calculate new case
class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        left = right = 0
        leftIndexes = []
        indexes = []
        max = 0
        for i in range(0,len(s)):
            if s[i] == '(' :
                leftIndexes.append(i)
            else : 
                if leftIndexes :
                    indexes.append((leftIndexes.pop(),i))
        indexes.sort(key=lambda tup: tup[0])
        if not indexes : return 0
        cur = indexes[0]
        for pivot in indexes :
            if pivot[0] == cur[1] + 1 : cur = (cur[0],pivot[1])
            elif pivot[0] > cur[1] + 1 : 
                if max < cur[1] - cur[0] + 1 : max = cur[1] - cur[0] + 1
                cur = pivot
        if max < cur[1] - cur[0] + 1 : max = cur[1] - cur[0] + 1
        return max    