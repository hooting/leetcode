class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            if all([ i < len(s) and s[i] == strs[0][i] for s in strs]):
                continue
            else:
                return strs[0][0:i]
        else:
            return strs[0]
        
        