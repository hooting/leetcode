class Solution {
public:
    int findMin(vector<int>& nums) {
        int size = nums.size();
        int min = INT_MAX;
        if(size == 0){
            return min;
        }
        int start = 0;
        int end = size - 1;
        int pivot;
        while(start < end){
            pivot = (start + end) / 2;
            if(nums[pivot] == nums[start]){
                min = min < nums[start] ? min : nums[start];
                if(pivot == start){
                    start = pivot + 1;
                }else{
                    if(nums[pivot - 1] == nums[pivot]){
                        start = pivot + 1;
                    }else{
                        //we can judge, the number from pivot to end is the same
                        end = pivot - 1;
                    }
                }
            }else if(nums[pivot] > nums[start]){
                //from the start to pivot, is in-order
                //the minimum is nums[start] or between
                //pivot + 1 to end;
                min = min < nums[start] ? min : nums[start];
                start = pivot + 1;
            }else{
                min = min < nums[pivot] ? min : nums[pivot];
                end = pivot - 1;
            }
        }
        min = min < nums[start] ? min : nums[start];
        return min;
    }
};