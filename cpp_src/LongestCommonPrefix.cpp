class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int size = strs.size();
        if(size == 0){
            return "";
        }
        sort(strs.begin(),strs.end());
        int length = strs[0].size();
        for(int i = 0; i < length; i++){
            if(strs[0][i] != strs[size - 1][i]){
                return strs[0].substr(0,i);
            }
        }
        return strs[0];
        
    }
};