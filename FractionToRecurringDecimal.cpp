/**
 * convert int to long, because of edge cases:[1,214748364],[-1,214748364],[1,-214748364],[-1,-214748364]
 * judge the result if negative or positive;
 * if it is negative, confirm that the factor is -0;
 * if the same remainder occures again, fractional part starts repeating
 */
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        long longDenominator = (long)denominator;
        long factor = numerator / longDenominator;
        long remainder = abs(numerator % longDenominator);
        string result;
        if(numerator * longDenominator < 0 && factor == 0){
            result = "-0";
        }else{
            result = std::to_string(factor);
        }
        if(remainder == 0){
            return result;
        }
        result += '.';
        longDenominator = abs(longDenominator);
        unordered_map<int,int> valueIndexMap;
        int index = result.size();
        int repeatIndex = 0;
        while(true){
            valueIndexMap[remainder] = index;
            remainder *= 10;
            factor = remainder / longDenominator;
            remainder %= longDenominator;
            result += std::to_string(factor);
            if(remainder == 0){
                return result;
            }
            repeatIndex = valueIndexMap[remainder];
            if(repeatIndex){
                result.insert(repeatIndex,"(");
                result += ')';
                return result;
            }
            index++;
        }
    }
};