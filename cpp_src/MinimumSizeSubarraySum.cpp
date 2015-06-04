class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int size = nums.size();
        int prePivot = -1;//the lastest number that we don't count
        int sum = 0;//the sum of counting number
        int minLength = 0x7fff - 1;
        int tempLength = 0;
        for(int i = 0; i < size; i++){
           sum += nums[i];
           if(sum >= s){
               while(prePivot < i && sum >= s){
                   //once the sum is bigger than or equal to s, 
                   //we should remove the pre number as more as possible 
                   sum -= nums[++prePivot];
               }
               // we need + 1 because we need the number on position prePivot.
               tempLength = i - prePivot + 1;
               minLength = minLength < tempLength ? minLength : tempLength;
           }
        }
        return minLength == (0x7fff - 1) ? 0 : minLength;
    }
};