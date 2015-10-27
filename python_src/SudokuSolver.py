class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        
    def solve(self, board):
        candidates = [str(x) for x in range(1,10)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for candidate in candidates:
                        if self.isLegal(board,i,j,candidate):
                            board[i][j] = candidate
                            if self.solve(board): return True
                    board[i][j] = '.'
                    return False
        return True
    
    def isLegal(self, board, row, column, candidate):
        for i in range(9):
            if board[row][i] == candidate: return False
            if board[i][column] == candidate: return False
        rowStart = row / 3 * 3
        columnStart = column / 3 * 3
        for i in range(rowStart,3 + rowStart):
            for j in range(columnStart,3 + columnStart):
                if board[i][j] == candidate: return False
        return True
        