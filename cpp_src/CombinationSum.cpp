class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        int size = candidates.size();
        if(size == 0 || target == 0){
            return result;
        }
        sort(candidates.begin(),candidates.end());
        vector<int> oneCase;
        recursive(candidates,0,target,oneCase,result);
        return result;
    }
    
    void recursive(vector<int>& candidates, int start, int target, vector<int>& oneCase, vector<vector<int>>& result){
        int size = candidates.size();
        for(int i = start; i < size; i++){
            target -= candidates[i];
            if(target < 0){
                return;
            }else if(target == 0){
                oneCase.push_back(candidates[i]);
                vector<int> final(oneCase);
                result.push_back(final);
                oneCase.pop_back();
                return;
            }else{
                oneCase.push_back(candidates[i]);
                recursive(candidates,i,target,oneCase,result);
            }
            target += candidates[i];
            oneCase.pop_back();
        }
    }
};