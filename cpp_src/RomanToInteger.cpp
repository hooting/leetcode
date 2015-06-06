/**
 * Roman：	 I		V		X		L		C		D		M
 * Integer: 1 		5 		10 		50 		100 	500 	1000
 */

class Solution {
public:
    int romanToInt(string s) {
        int result = 0;
        int size = s.size();
        int sameTime = 0;
        map<char,int> romanInt = {{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};
        for(int i = 0; i < size; i++){
            result += romanInt[s[i]];
            if(i > 0){
                if(s[i] == s[i - 1]){
                    sameTime++;
                }else{
                    if(romanInt[s[i]] > romanInt[s[i - 1]]){
                        result -= sameTime * romanInt[s[i - 1]] * 2;
                    }  
                    sameTime = 1;
                }
            }else{
                sameTime++;
            }
        }
        return result;
    }
};