"""
 reference to https://leetcode.com/discuss/20151/an-o-n-solution-with-detailed-explanation
 given a sliding window with size lenW
 if the sliding window matches in s, then slide the window with step lenW
 else remove the previous matched window
"""
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        dic = {}
        result = []
        for word in words:
            if word in dic: dic[word] += 1
            else: dic[word] = 1
        wordNum = len(words)
        lenW = len(words[0])
        lenS = len(s)
        for i in range(lenW):
            count = 0
            foundDic = {}
            left = i
            for j in range(i,lenS - lenW + 1,lenW):
                sub = s[j:j+lenW]
                if sub in dic:
                    count += 1
                    if sub in foundDic:
                        foundDic[sub] += 1
                    else:
                        foundDic[sub] = 1
                    while foundDic[sub] > dic[sub]:
                        removeSub = s[left:left+lenW]
                        foundDic[removeSub] -= 1
                        count -= 1
                        left += lenW
                    if count == wordNum:
                        result.append(left)
                        removeSub = s[left:left+lenW]
                        foundDic[removeSub] -= 1
                        count -= 1
                        left += lenW
                else:
                    count = 0
                    foundDic = {}
                    left = j + lenW
        return result
                
        