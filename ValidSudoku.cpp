/**
 * reference to https://leetcode.com/discuss/23901/my-short-solution-by-c-o-n2
 * The problem requires us only check 9 sub-squares marked by bold black lines,
 * rather than all possible 3*3 sub-squares.
 * As number used in Sudoku can only be 1-9, the size of board is at most 9*9
 *
 */
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int rows = board.size();
        if(rows == 0){
            return true;
        }
        int columns = board[0].size();
        if(columns == 0){
            return true;
        }
        int valid1[9][9] = {0};//for each row
        int valid2[9][9] = {0};//for each column
        int valid3[9][9] = {0};//for each sub-box
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < columns; j++){
                if(board[i][j] != '.'){
                    int num = board[i][j] - '0' - 1;
                    int ithSubBox = (i / 3) * 3 + j / 3;
                    if(valid1[i][num] || valid2[j][num] || valid3[ithSubBox][num]){
                        return false;
                    }
                    valid1[i][num] = 1;
                    valid2[j][num] = 1;
                    valid3[ithSubBox][num] = 1;
                }
            }
        }
        return true;
    }
};