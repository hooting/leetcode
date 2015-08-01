class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> result;
        int size = words.size();
        for(int i = 0,k,l; i < size; i += k){
            for(k = l = 0; k + i < size && l + words[k+i].size() + k <= maxWidth; k++)
                l += words[k+i].size();
            int spaceNums = maxWidth - l;
            if (k + i == size){
                string temp = words[i];
                for(int j = 1; j < k; j++){
                    temp += " " + words[i + j];
                }
                temp += string(maxWidth - temp.size(), ' ');
                result.push_back(temp);
            }else{
                if(k == 1){
                    string temp = words[i] + string(maxWidth - words[i].size(),' ');
                    result.push_back(temp);
                }else{
                    int averageSpace = spaceNums / (k - 1);
                    string temp = words[i];
                    int j = 0;
                    for(j = 0; j < spaceNums % (k - 1); j++){
                        temp += string(averageSpace + 1, ' ');
                        temp += words[i + 1 + j];
                    }
                    for(j++; j < k;j++){
                        temp += string(averageSpace, ' ');
                        temp += words[i + j];
                    }
                    result.push_back(temp);
                }
            }
        }
        return result;
    }
};