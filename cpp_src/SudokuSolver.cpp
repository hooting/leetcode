class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        int rows = board.size();
        if(rows == 0) return;
        int columns = board[0].size();
        if(columns == 0) return;
        solve(board,rows,columns);
    }
    
    bool solve(vector<vector<char>>& board, int rows, int columns){
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < columns; j++){
                if(board[i][j] == '.'){
                    for(char k = '1'; k <= '9'; k++){
                        if(isValid(board,i,j,k)){
                            board[i][j] = k;
                            if(solve(board,rows,columns)) return true;
                        }
                    }
                    board[i][j] = '.';
                    return false;
                }
            }
        }
        return true;//You may assume that there will be only one unique solution.
    }
    
    //this efficiency of the very important, otherwise TLE occurs
    bool isValid(vector<vector<char>>& board,int row, int column, char k){
        for(int i = 0; i < 9; i++){
            //check the row
            if(board[row][i] == k) return false;
            
            //check the column
            if(board[i][column] == k) return false;
        }
        
        int subBoxRow = row / 3 * 3;
        int subBoxColumn = column / 3 * 3;
        for(int i = subBoxRow; i < subBoxRow + 3; i++){
            for(int j = subBoxColumn; j < subBoxColumn + 3; j++){
                if(board[i][j] == k) return false;
            }
        }
        return true;
    }
};