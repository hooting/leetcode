class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        if(size <= 1){
            return 0;
        }
        int boughtPrice, total = 0;
        bool bought = false;
        for(int i = 0; i < size - 1; i++){
            if(prices[i] < prices[i+1]){
                if(!bought){
                    boughtPrice = prices[i];
                    bought = true;
                }
            }else if(prices[i] == prices[i+1]){
                continue;
            }else{
                if(bought){
                    total += prices[i] - boughtPrice;
                    bought = false;
                }
            }
        }
        if(bought){
            total += prices[size - 1] - boughtPrice;
        }
        return total;
    }
};