class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        factorial = {}
        base = 1
        for i in range(1,n):
            base *= i
            factorial[i] = base
        result = []
        candidates = range(1,n+1)
        while k > 1:
            divisor = factorial[len(candidates) - 1]
            a,k = divmod(k,divisor)
            if a == len(candidates):
                candidates.reverse()
                break
            if k == 0:
                result.append(candidates[a - 1])
                del  candidates[a - 1]
                candidates.reverse()
                break
            result.append(candidates[a])
            del candidates[a]
        result += candidates
        result = [str(x) for x in result]
        return "".join(result)

