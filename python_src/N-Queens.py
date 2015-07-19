class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        if n == 0:return list()
        row_marks = [0] * n
        column_marks = [0] * n
        #row + column is equal if in the same diagonal
        diagonal_marks = [0] * (2 * n - 1)
        #row - column is equal if in the same opposite diagonal
        opposite_marks = [0] * (2 * n - 1)
        result = []
        one_case = [["."] * n for x in range(0,n)]
        self.recursive(n,column_marks,diagonal_marks,opposite_marks,0,result,one_case)
        return result
    
    def recursive(self,n,column_marks,diagonal_marks,opposite_marks,row,result,one_case):
        for i in range(0,n):
            if column_marks[i] == diagonal_marks[row + i] == opposite_marks[row - i + n - 1] == 0:
                one_case[row][i] = 'Q'
                if row == n - 1:
                    one_result = ["".join(a) for a in one_case]
                    result.append(one_result)
                    one_case[row][i] = '.'
                    return
                else:
                    column_marks[i] = diagonal_marks[row + i] = opposite_marks[row - i + n - 1] = 1
                    self.recursive(n,column_marks,diagonal_marks,opposite_marks,row+1,result,one_case)
                    column_marks[i] = diagonal_marks[row + i] = opposite_marks[row - i + n - 1] = 0
                    one_case[row][i] = '.'
                
        
        
        
        