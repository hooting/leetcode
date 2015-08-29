public class Solution {
    public int missingNumber(int[] nums) {
        if(nums == null){
            return -1;
        }
        int size = nums.length;
        int totalSum = (0 + size) * (size+1) / 2;
        int sum = 0;
        for(int i = 0; i < size; i++){
            sum += nums[i];
        }
        return totalSum - sum;
    }
}