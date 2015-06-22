class Solution {
public:
    int strStr(string haystack, string needle) {
        int haystackSize = haystack.size();
        int needleSize = needle.size();
        if(needleSize == 0){
            return 0;
        }
        int last = haystackSize - needleSize;
        int i,j;
        for(i = 0; i <= last; i++){
            for(j = 0; j < needleSize; j++){
                if(haystack[i + j] != needle[j]) break;
            }
            if(j == needleSize){
                return i;
            }
        }
        return -1;
    }
};