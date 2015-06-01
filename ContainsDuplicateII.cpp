class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int,int> numIndexMap;
        map<int,int>::iterator it;
        int size = nums.size();
        for(int i; i < size; i++){
            it = numIndexMap.find(nums[i]);
            if(it == numIndexMap.end()){
                numIndexMap[nums[i]] = i; 
            }else{
                if(i - it->second <= k){
                    return true;
                }else{
                    numIndexMap[nums[i]] = i;
                }
            }
        }
        return false;
    }
};