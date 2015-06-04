class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        if(matrix.size() == 0){
            return result;
        }
        int top = 0;
        int buttom = matrix.size() - 1;
        int left = 0;
        int right = matrix[0].size() - 1;
        while(top <= buttom && left <= right){
            if(top == buttom){
                for(int i = left; i <= right; i++){
                    result.push_back(matrix[top][i]);
                }
                break;
            }
            if(left == right){
                for(int i = top; i <= buttom; i++){
                    result.push_back(matrix[i][left]);
                }
                break;
            }
            for(int i = left; i < right; i++){
                result.push_back(matrix[top][i]);
            }
            for(int i = top; i < buttom; i++){
                result.push_back(matrix[i][right]);
            }
            for(int i = right; i > left; i--){
                result.push_back(matrix[buttom][i]);
            }
            for(int i = buttom; i > top; i--){
                result.push_back(matrix[i][left]);
            }
            left++;
            right--;
            top++;
            buttom--;
        }
        return result;
    }
};