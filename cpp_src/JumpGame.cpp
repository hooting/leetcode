class Solution {
public:
    bool canJump(vector<int>& nums) {
        int size = nums.size();
        if(size <= 1){
            return true;
        }
        int maxIndex = 0;//the max index we can reach index i;
        for(int i = 0; i < size; i++){
            if(maxIndex < i){
                return false;
            }else{
                maxIndex = maxIndex > i + nums[i] ? maxIndex : i + nums[i];   
            }
        }
        if(maxIndex >= size -1){
            return true;
        }else{
            return false;
        }
    }
};