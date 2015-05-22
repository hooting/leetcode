class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> result;
        if(n == 0){
            return result;
        }
        vector<int> *row;
        for(int i = 0; i < n; i++){
            row = new vector<int>(n);
            result.push_back(*row);
        }
        int value = 1;
        int top = 0;
        int buttom = n - 1;
        int left = 0;
        int right = n - 1;
        while(top < buttom && left < right){
            for(int i = left; i < right; i++){
                result[top][i] = value++;
            }
            for(int i = top; i < buttom; i++){
                result[i][right] = value++;
            }
            for(int i = right; i > left; i--){
                result[buttom][i] = value++;
            }
            for(int i = buttom; i > top; i--){
                result[i][left] = value++;
            }
            left++;
            right--;
            top++;
            buttom--;
        }
        if(top == buttom){
            for(int i = left; i <= right; i++){
                result[top][i] = value++;
            }
        }else{
            for(int i = top; i <= buttom; i++){
                result[i][left] = value++;
            }
        }
        return result;
    }
};