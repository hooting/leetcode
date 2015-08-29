/**
 * reference to https://leetcode.com/discuss/52351/accepted-java-space-easy-solution-with-detail-explanations
 * 
 */ 
public class Solution {
    public int[] singleNumber(int[] nums) {
        int result = 0;
        for(int value : nums){
            result ^= value;
        }
        result &= - result;
        int[] ret = {0,0};
        for(int value : nums){
            if((value & result) == 0){
                ret[0] ^= value;
            }else{
                ret[1] ^= value;
            }
        }
        return ret;
    }
}