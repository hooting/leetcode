class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        if(n <= 0) return result;
        recursive(result,"",0,0,n);
        return result;
    }
    
    void recursive(vector<string>& result, string part, int left,int right, int n){
        if(left >= n){
            part.append(n - right,')');
            result.push_back(part);
            return;
        }
        part.push_back('(');
        recursive(result,part,left+1,right,n);
        if(left > right){
            part.pop_back();
            part.push_back(')');
            recursive(result,part,left,right+1,n);
        }
    }
    
};