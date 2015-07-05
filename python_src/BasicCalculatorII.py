class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        stack = []
        s += " "
        size = len(s)
        start = 0
        for i in range(0,size):
            if s[i] == ' ':
                if start < i:
                    stack.append(s[start:i])
                    self.multiDiv(stack)
            elif s[i] == '+' or s[i] == '-':
                if start < i:
                    stack.append(s[start:i])
                    self.multiDiv(stack)
                stack.append(s[i])
            elif s[i] == '*' or s[i] == '/':
                if start < i:
                    stack.append(s[start:i])
                    self.multiDiv(stack)
                stack.append(s[i])
            else: continue
            start = i + 1
        if not stack: return 0
        result = int(stack[0])
        i = 1
        while i < len(stack):
            if stack[i] == '+':
                result += int(stack[i+1])
            else:
                result -= int(stack[i+1])
            i += 2
        return result 
        
    def multiDiv(self,stack):
        try:
            a = int(stack[-3])
            op = stack[-2]
            b = int(stack[-1])
            if op == '*':
                del stack[-3:]
                stack.append(a * b)
            elif op == '/':
                del stack[-3:]
                stack.append(a / b)
        except IndexError:pass
                