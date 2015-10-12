class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for item in s:
            if item in ['[','(','{']:
                stack.append(item)
            else:
                if len(stack) == 0: return False
                if item == ']' and stack[-1] == '[':
                    del stack[-1]
                elif item == ')' and stack[-1] == '(':
                    del stack[-1]
                elif item == '}' and stack[-1] == '{':
                    del stack[-1]
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                    