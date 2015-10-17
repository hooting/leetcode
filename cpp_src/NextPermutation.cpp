/**
 * a1,a2,a3,a4,a5,...,aN
 * find such a pair (ai,aj),
 * where ai < aj.
 * if there are many such pairs,
 * then find out the pair, where i is maxium
 * if there are many such pairs, (i,j1),(i,j2),....
 * then find out the pair, where num[jx] is minimum
 * swap(i,jx);
 * after above operations
 * we have to sort(i+1,end);
 * 
 */
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int length = nums.size();
        if(length == 0){
            return;
        }
        int max = nums[length - 1] - 1;
        int rightPivot = length;
        int leftPivot = 0;
        bool found = false;
        for(int i = length - 1; i >= 1; i--){
            if(nums[i] < max){
                continue;
            }
            for(int j = i - 1; j >= leftPivot; j--){
                if(nums[i] > nums[j]){
                    if(!found){
                        rightPivot = i;
                        leftPivot = j;
                    }else{
                        if(leftPivot == j){
                            rightPivot = nums[i] < nums[rightPivot] ? i : rightPivot;
                        }else{
                            rightPivot = i;
                            leftPivot = j;
                        }
                    }
                    found = true;
                }
            }
            max = nums[i] > max ? nums[i] : max;
        }
        if(found){
            int temp = nums[rightPivot];
            nums[rightPivot] = nums[leftPivot];
            nums[leftPivot] = temp;
            sort(nums.begin() + leftPivot + 1, nums.end());
        }else{
            sort(nums.begin(),nums.end());
        }
    }
};
