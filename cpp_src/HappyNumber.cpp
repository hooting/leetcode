class Solution {
public:
    bool isHappy(int n) {
        if(n <= 0){
            return false;
        }
        unordered_map<int,int> dictionary;
        for(int i = 0; i < 10; i++){
            dictionary[i] = i * i;
        }
        set<int> visitedSet;
        visitedSet.insert(n);
        while(true){
            int total = 0;
            while(n > 0){
                total += dictionary[n % 10];
                n /= 10;
            }
            if(total == 1){
                return true;
            }else{
                if(visitedSet.find(total) == visitedSet.end()){
                    visitedSet.insert(total);
                    n = total;
                }else{
                    return false;
                }
            }
        }
    }
};