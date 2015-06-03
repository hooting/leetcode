class Solution {
public:
    vector<string> anagrams(vector<string>& strs) {
        map<string, vector<string>*> strGroupMap;
        vector<string> result;;
        for(string str : strs){
            string original(str);
            sort(str.begin(),str.end());
            vector<string>* vec = strGroupMap[str];
            if(vec == NULL){
                vec = new vector<string>();
            }
            vec->push_back(original);
            strGroupMap[str] = vec;
        }
        map<string, vector<string>*>::iterator ite;
        for(ite = strGroupMap.begin(); ite != strGroupMap.end(); ite++){
            if(ite->second->size() > 1){
                vector<string>::iterator eleIte;
                for(eleIte = ite->second->begin(); eleIte != ite->second->end(); eleIte++){
                    result.push_back(*eleIte);
                }
            }
        }
        return result;
    }
};