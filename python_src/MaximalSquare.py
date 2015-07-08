#reference https://leetcode.com/discuss/38489/easy-solution-with-detailed-explanations-8ms-time-and-space
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        rows = len(matrix)
        if rows == 0: return 0
        columns = len(matrix[0])
        if columns == 0: return 0
        grids = [[0 for x in range(0,columns)] for x in range(0,rows)]
        maxEdge = 0
        for i in range(0,columns):
            grids[0][i] = int(matrix[0][i])
            maxEdge = max(maxEdge,grids[0][i])
        for i in range(0,rows):
            grids[i][0] = int(matrix[i][0])
            maxEdge = max(maxEdge,grids[i][0])
        for i in range(1,rows):
            for j in range(1,columns):
                if matrix[i][j] == '0':
                    grids[i][j] = 0
                else:
                    grids[i][j] = min(grids[i-1][j],grids[i][j-1],grids[i-1][j-1]) + 1
                    maxEdge = max(maxEdge,grids[i][j])
        return maxEdge * maxEdge
