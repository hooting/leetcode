/**
 * reference to https://leetcode.com/discuss/24478/i-did-it-in-10-lines-of-c
 * The main idea is to store the substring as int in map to bypass the memory limits.
 * There are only four possible character A, C, G, and T, but I want to use 3 bits per letter instead of 2.
 * A is 0101, C is 0103, G is 0107, T is 0124. The last digit in octal are different for all four letters. 
 */
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> result;
        unordered_map<int,int> timeMap;
        int size = s.size();
        if(size <= 10){
            return result;
        }
        int i = 0;
        int pattern = 0;
        //get the first 10 letters
        while(i < 10){
            pattern = (pattern << 3) | (s[i] & 7);
            i++;
        }
        timeMap[pattern]++;
        while(i < size){
            //move out the first letter of sub string
            //append the following letter;
            pattern = (pattern << 3 & 0x3FFFFFFF) | (s[i] & 7);
            i++;
            timeMap[pattern]++;
            if(timeMap[pattern] == 2){
                result.push_back(s.substr(i-10,10));
            }
        }
        return result;
        
    }
};