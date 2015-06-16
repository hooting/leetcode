class Solution {
public:
    string countAndSay(int n) {
        string result;
        if(n <= 0) return result;
        result.append(1,'1');
        for(int i = 1; i < n; i++){
            string temp;
            int time = 1;
            char c = result[0];
            int size = result.size();
            for(int j = 1; j < size; j++){
                if(c == result[j]) time++;
                else{
                    temp.append(1,time+'0');
                    temp.append(1,c);
                    c = result[j];
                    time = 1;
                }
            }
            temp.append(1,time+'0');
            temp.append(1,c);
            result = temp;
        }
        return result;
    }
};