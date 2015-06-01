class Solution {
public:
    int countPrimes(int n) {
        if(n <= 2){
            return 0;
        }
        vector<int> primes;
        primes.push_back(2);
        int i = 3; 
        int flag = true;
        while(i < n){
            flag = true;
            int value = sqrt(i);
            for(int prime : primes){
                
                if(i % prime == 0){
                    flag = false;
                    break;
                }
                if(prime > value){
                    break;
                }
            }
            if(flag){
                primes.push_back(i);
            }
            i+=2;
        }
        return primes.size();
    }
};