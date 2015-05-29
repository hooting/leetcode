/**
 * reference to https://leetcode.com/discuss/18886/my-really-simple-java-o-n-solution-accepted
 * We will use HashMap. 
 * The key thing is to keep track of the sequence length and store that in the boundary points of the sequence. 
 * For example, as a result, for sequence {1, 2, 3, 4, 5}, map.get(1) and map.get(5) should both return 5.
 */
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int,int> map;//initiate the value to 0;
        int ret = 0;
        for(int i : nums){
            if(map[i])// This means we have already check i before
                continue;
            map[i] = map[i - 1] + map[i + 1] + 1;
            map[i - map[i - 1]] = map[i];
            map[i + map[i + 1]] = map[i];
            ret = max(ret, map[i]);
        }
        return ret;
    }
};