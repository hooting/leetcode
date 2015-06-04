class Solution {
public:
    string longestPalindrome(string s) {
        int size = s.size();
        if(size <= 1) return s;
        int pivot = 0;
        int maxLen = 0;
        int maxLeft = 0;
        while(pivot < size){
            int left = pivot - 1, right = pivot + 1;
            while(right < size && s[right] == s[right - 1]) right++;
            pivot = right;
            while(left >= 0 && right < size && s[left] == s[right]){
                left--;
                right++;
            }
            int tempLen = (right - 1) - (left + 1) + 1;
            if(maxLen < tempLen){
                maxLen = tempLen;
                maxLeft = left + 1;
            }
        }
        return s.substr(maxLeft,maxLen);
    }
};