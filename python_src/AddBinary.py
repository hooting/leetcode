class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        lenA = 0 - len(a)
        lenB = 0 - len(b)
        carryBit,result = 0, []
        start = -1
        while start >= lenA and start >= lenB:
            carryBit += int(a[start]) + int(b[start])
            result.append(str(carryBit % 2))
            carryBit /= 2
            start -= 1
        if start >= lenA:
            while start >= lenA:
                carryBit += int(a[start])
                result.append(str(carryBit % 2))
                carryBit /= 2
                start -= 1
        else:
            while start >= lenB:
                carryBit += int(b[start])
                result.append(str(carryBit % 2))
                carryBit /= 2
                start -= 1
        if carryBit == 1:
            result.append(`1`)
        result = reversed(result)
        return "".join(result)
        