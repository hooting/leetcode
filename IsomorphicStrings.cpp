class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int size = s.size();
        if(size != t.size()){
            return false;
        }
        unordered_map<char, char> map;
        //charSet is used to avoid two characters may map to the same character
        set<char> charSet;
        //use t's character to replace s'
        for(int i = 0; i < size; i++){
            //we should use t[i] to replace s[i]
            if(s[i] != t[i]){
                //we have not replace s[i] before.
                if(map.find(s[i]) == map.end()){
                    //we have not use t[i] to replace any of s' character
                    if(charSet.find(t[i]) == charSet.end()){
                        map[s[i]] = t[i];
                        charSet.insert(t[i]);
                    }else{
                        return false;
                    }
                }else{
                    //the same s[i] maps to different t[i]
                    if(map[s[i]] != t[i]){
                        return false;
                    }
                }
            }else{
                //we have replace s[i] before, but the previous is not equal to t[i]
                if(map.find(s[i]) != map.end() && map[s[i]] != t[i]){
                    return false;
                }
                map[s[i]] = t[i];
                charSet.insert(t[i]);
            }
        }
        return true;
    }
};