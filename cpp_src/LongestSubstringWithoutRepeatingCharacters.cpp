class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> positions;
        int size = s.size();
        if(size == 0){
            return 0;
        }
        int maxLength = 0;
        int startIndex = 0;//store the start index of sub string
        map<char,int>::iterator it;
        for(int i = 0; i < size; i++){
            it = positions.find(s[i]);
            if(it == positions.end() || it->second < startIndex){
                //no repeat character appeared in our focus sub string, where start at startIndex
                positions[s[i]] = i;
            }else{
                //repeat charater appeared, store the max length(not include i), 
                //and start next to the repeat charater
                maxLength = maxLength > (i - startIndex) ? maxLength : (i - startIndex);
                startIndex = it->second + 1;
                positions[s[i]] = i;
            }
        }
        maxLength = maxLength > (size - startIndex)? maxLength : (size - startIndex);
        return maxLength;
    }
};