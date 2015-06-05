class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows <= 0){
            return "";
        }else if(numRows == 1){
            return s;
        }
        string* rows = new string[numRows];
        int size = s.size();
        int rowIndex = 0;
        bool isDown = false;
        for(int i = 0; i < size; i++){
            rows[rowIndex].push_back(s[i]);
            if(rowIndex == numRows - 1 && isDown == true){
                isDown = false;
            }else if(rowIndex == 0 && isDown == false){
                isDown = true;
            }
            if(isDown){
                rowIndex++;
            }else{
                rowIndex--;
            }
        }
        string result;
        for(int i = 0; i < numRows; i++){
            result.append(rows[i]);
        }
        delete []rows;
        return result;
    }
};