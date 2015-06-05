class Solution {
public:
    int myAtoi(string str) {
        int size = str.size();
        if(size == 0){
            return 0;
        }
        
        int startIndex = 0;
        while(startIndex < size && str[startIndex] == ' '){
            startIndex++;
        }
        bool negative = str[startIndex] == '-' ? true : false;
        if(str[startIndex] == '-' || str[startIndex] == '+'){
            startIndex++;
        }
        long value = 0;
        while(startIndex < size){
            if(str[startIndex] > '9' || str[startIndex] < '0'){
                return negative ? (int)-value : (int)value;;
            }else{
                value = value * 10 + str[startIndex] - '0';
                startIndex++;
            }
            if(negative){
                if(-value < INT_MIN){
                    return INT_MIN;
                }
            }else{
                if(value > INT_MAX){
                    return INT_MAX;
                }
            }
        }
        return negative ? (int)-value : (int)value;
    }
};