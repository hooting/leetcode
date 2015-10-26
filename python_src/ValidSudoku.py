class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        subs = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                value = int(board[i][j]) - 1
                subIth = (i / 3) * 3 + j / 3
                
                if rows[i][value] == 1 or columns[j][value] == 1 or subs[subIth][value] == 1:
                    return False
                else:
                    rows[i][value] = 1
                    columns[j][value] = 1
                    subs[subIth][value] = 1
        return True