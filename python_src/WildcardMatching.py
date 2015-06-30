class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        starNum = 0
        for c in p:
            if c == '*': starNum += 1
        i = j = 0
        lenS = len(s)
        lenP = len(p)
        while i < lenS and j < lenP:
            if p[j] == '*':
                starNum -= 1 # remain starNum '*'s in the rest of p
                count = 0
                while j + 1 < lenP:
                    if p[j + 1] == '?':
                        count += 1
                    elif p[j + 1] == '*':
                        starNum -= 1
                    else: break
                    j += 1
                j += 1 # j point to the first non-'*' and non-'?' character
                if j == lenP:
                    if count <= lenS - i:return True 
                    #there must be more than count charaters in s to match '?' in p
                    else: return False
                else:
                    if starNum == 0: # there is no '*' in the rest of p
                        i += count #need count charaters in s to match '?' in p
                        if lenS - i < lenP - j:return False
                        #the length of rest of s is less than the length of rest of p
                        #thus, they can't be matched
                        else:
                            #try to match the rest (lenP - j) charaters
                            i = lenS - (lenP - j)
                            continue
                    k = j
                    while k < lenP and p[k] != '*' and p[k] != '?':
                        k +=1
                    #find the sub in the rest of s
                    sub = p[j:k]
                    if k == lenP: 
                        if s.endswith(sub): return True
                        else: return False
                    i += count
                    i = s.find(sub,i)
                    if i == -1: return False
                    else:
                        i += k - j
                        j = k
            elif s[i] == p[j] or p[j] == '?':
                i += 1
                j += 1
            else: return False
        if j == lenP and i < lenS: return False
        while j < lenP:
            if p[j] == '*': j += 1
            else: return False
        return True