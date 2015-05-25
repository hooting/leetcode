class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        if(size <= 1){
            return 0;
        }
        int buyPrice = INT_MAX;
        int maxProfit = 0;
        bool bought = false;
        for(int i = 0; i < size; i++){
            if(prices[i] <= prices[i+1]){
                if(!bought){
                    buyPrice = buyPrice < prices[i] ? buyPrice : prices[i];
                    bought = true;
                }
            }else{
                if(bought){
                    maxProfit = maxProfit > prices[i] - buyPrice ? maxProfit : prices[i] - buyPrice;
                    bought = false;
                }
            }
        }
        if(bought){
            maxProfit = maxProfit > prices[size - 1] - buyPrice ? maxProfit : prices[size - 1] - buyPrice;
        }
        return maxProfit;
    }
};