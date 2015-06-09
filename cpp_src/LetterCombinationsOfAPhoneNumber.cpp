class Solution {
public:
    vector<string> letterCombinations(string digits) {
        //we assume there are only 2-9 in digits;
        map<char,set<char>> numToChar;
        numToChar['2'] = {'a','b','c'};
        numToChar['3'] = {'d','e','f'};
        numToChar['4'] = {'g','h','i'};
        numToChar['5'] = {'j','k','l'};
        numToChar['6'] = {'m','n','o'};
        numToChar['7'] = {'p','q','r','s'};
        numToChar['8'] = {'t','u','v'};
        numToChar['9'] = {'w','x','y','z'};
        vector<string>* result = new vector<string>();
        int size = digits.size();
        for(int i = 0; i < size; i++){
            if(result->size() == 0){
                for(char c : numToChar[digits[i]]){
                    string s(1,c);
                    result->push_back(s);
                }
            }else{
                vector<string>* temp = new vector<string>();
                for(string s : *result){
                    for(char c : numToChar[digits[i]]){
                        string newS(s);
                        newS.append(1,c);
                        temp->push_back(newS);
                    }
                }
                delete result;
                result = temp;
            }
        }
        return *result;
    }
};