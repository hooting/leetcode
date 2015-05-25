/**
 * if i < j then steps[i] <= steps[j]
 */
class Solution {
public:
    int jump(vector<int>& nums) {
        int size = nums.size();
        if(size <= 1){
            return 0;
        }
        int steps[size];
        steps[0] = 0;
        for(int i = 1; i < size; i++){
            steps[i] = INT_MAX;
        }
        int maxIndex;
        int preMaxIndex = 0;
        for(int i = 0; i < size; i++){
            maxIndex = i + nums[i];
            if(maxIndex >= size - 1){
                //we already reach the last index
                return steps[i] + 1;
            }
            // when index i = x, index between x+1 to preMaxIndex, 
            //its minimum step has already been calculated, when i = x - 1;
            for(int j = preMaxIndex; j <= maxIndex; j++){
                steps[j] = steps[j] < steps[i] + 1 ? steps[j] : steps[i] + 1;
            }
            preMaxIndex = maxIndex;
        }
        return steps[size - 1];
    }
};