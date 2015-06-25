class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if s == "":
            return 0
        strLen = len(s)
        wordLen = 0
        temp = 0
        for c in s:
            if c == ' ':
                if temp != 0:
                    wordLen = temp
                temp = 0
            else:
                temp += 1
        if temp == 0:
            return wordLen
        else:
            return temp