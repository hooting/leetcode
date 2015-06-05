class Solution {
public:
    int reverse(int x) {
        bool negative = x < 0 ? true : false;
        x = x < 0 ? -x : x;
        long reversed = 0;
        while(x > 0){
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }
        reversed = negative ? -reversed : reversed;
        if(reversed > INT_MAX || reversed < INT_MIN){
            return 0;
        }else{
            return (int)reversed;
        }
    }
    bool isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        int y = reverse(x);
        return y == x;
    }
};