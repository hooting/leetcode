class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")
        v11 = []
        v21 = []
        for s in v1:
            s = s.lstrip('0')
            if not s: v11.append(0)
            else: v11.append(int(s))
        for s in v2:
            s = s.lstrip('0')
            if not s: v21.append(0)
            else: v21.append(int(s))
        v1 = v11
        v2 = v21
        len1 = len(v1)
        len2 = len(v2)
        i = 0
        while i < len1 and i < len2:
            if v1[i] > v2[i]: return 1
            elif v1[i] < v2[i]: return -1
            else:
                i += 1
        if len1 < len2: 
            while i < len2:
                if v2[i] != 0: return -1
                i += 1
            return 0
        elif len1 == len2: return 0
        else:
            while i < len1:
                if v1[i] != 0: return 1
                i += 1
            return 0
            