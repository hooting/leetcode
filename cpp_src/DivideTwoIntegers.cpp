/**
 * -2147483648, -1
 * overflow
 */
class Solution {
public:
    int divide(int dividend, int divisor) {
        if(divisor == 0) return INT_MAX;
        bool negative = false;
        long dividendL = (long)dividend;
        long divisorL = (long)divisor;
        if((dividendL > 0 && divisorL < 0) || (dividendL < 0 && divisorL > 0)) negative = true;
        if(dividendL < 0) dividendL = -dividendL;
        if(divisorL < 0) divisorL = -divisorL;
        long result = 0;
        long temp = 0;
        do{
            result += expand(dividendL,divisorL,temp);
            dividendL = temp;
        }while(dividendL >= divisorL);
        if(negative) return (int)-result;
        else{
            if(result > INT_MAX) return INT_MAX;
            else return (int)result;
        }
    }
    
    //each time, we minus divisor^n, where n is the max integer that satisfies divisor^n < dividend,
    //the factor should be 2^n.
    int expand(long dividend, long divisor,long& mod){
        if(dividend < divisor){
            return 0;
        }
        int n = 0;
        while(dividend >= divisor){
            n++;
            divisor = divisor << 2;
        }
        mod = dividend - (divisor >> 2);
        n--;
        int result = 1;
        for(int i = 0; i < n; i++){
            result = result << 2;
        }
        return result;
    }
};