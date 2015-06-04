class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> result;
        vector<int> oneCase;
        recursive(1,k,n,oneCase,result);
        return result;
    }
    
    void recursive(int start, int k, int n, vector<int> oneCase, vector<vector<int>>& result){
        if(start > 9 || k < 1){
            return;
        }
        for(int i = start; i < 10; i++){
            if(i > n){
                return;
            }else if(i == n){
                if(k == 1){
                    oneCase.push_back(i);
                    vector<int> final(oneCase);
                    result.push_back(final);
                    oneCase.pop_back();
                }else{
                    return;
                }
            }else{
                oneCase.push_back(i);
                recursive(i+1,k-1,n - i, oneCase,result); 
                oneCase.pop_back();
            }
        }
    }
};