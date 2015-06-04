/**
 * reference to http://stackoverflow.com/questions/1586858/find-the-smallest-integer-not-in-a-list
 * if there is no missing positive integer,
 * then the array should be like
 * nums[0] = 1; nums[1] = 2; nums[2] = 3; ... ; nums[size -1] = size;
 * we take advantage of this charater,
 * if nums[i](represent pivot) is between 1 to size;
 * then put it in nums[pivot -1]
 * After that, go through the whole array, the first element which i != nums[i-1],return i;
 * 
 * the comparation time of while is summer to N;
 * because at most N number need to update their positions.
 */
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int size = nums.size();
        if(size == 0){
            return 1;
        }
        int pivot;
        int index;
        for(int i = 0; i < size; i++){
            pivot = nums[i];
            while(!(pivot > size || pivot < 1 || pivot == nums[pivot - 1])){
                index = pivot - 1;
                pivot = nums[index];
                nums[index] = index + 1;
            }
        }
        for(int i = 0; i< size; i++){
            if(nums[i] != i + 1){
                return i+1;
            }
        }
        return size+1;
    }
};