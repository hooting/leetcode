class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        digits = ('0','1','2','3','4','5','6','7','8','9')
        stack = []
        s += " "
        size = len(s)
        start = 0
        for i in range(0,size):
            if s[i] == '(':
                if i > start:
                    stack.append(s[start:i])
                self.getOne(stack)
                stack.append(s[i])
            elif s[i] == ' ':
                if i > start:
                    stack.append(s[start:i])
                self.getOne(stack)
            elif s[i] == '+' or s[i] == '-':
                if i > start:
                    stack.append(s[start:i])
                self.getOne(stack)
                stack.append(s[i])
            elif s[i] == ')':
                if i > start:
                    stack.append(s[start:i])
                self.getOne(stack)
                del stack[-2]
            elif s[i] in digits: continue
            start = i + 1
        if not stack: return int(s)
        else: return int(stack[0])
            
    def getOne(self, stack):
        try:
            a = int(stack[-3])
            op = stack[-2]
            b = int(stack[-1])
            if op == '+':
                result = a + b
                del stack[-3:]
                stack.append(result)
            elif op == '-':
                result = a - b
                del stack[-3:]
                stack.append(result)
        except (IndexError, ValueError): pass   
                
                    