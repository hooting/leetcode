/**
 * reference to 
 * https://github.com/hooting/haoelleetcode/blob/master/src/bestTimeToBuyAndSellStock/bestTimeToBuyAndSellStock.III.cpp
 * Dynamic Programming
 * 
 * Considering prices[n], and we have a position "i", we could have
 *      1) the maxProfit1 for prices[0..i]  
 *      2) the maxProfit2 for proices[i..n]
 * 
 * So, 
 *  for 1) we can go through the prices[n] forwardly.
 *      forward[i] = max( forward[i-1], price[i] - lowestPrice[0..i] ) 
 *  for 2) we can go through the prices[n] backwoardly.
 *      backward[i] = max( backward[i+1], highestPrice[i..n] - price[i]) 
 */
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        if(size <= 1){
            return 0;
        }
        int* forward = new int[size];
        int* backward = new int[size];
        int min = prices[0];
        forward[0] = 0;
        for(int i = 1; i < size; i++){
            min = min < prices[i] ? min : prices[i];
            forward[i] = forward[i-1] > prices[i] - min ? forward[i-1] : prices[i] - min;
        }
        int max = prices[size - 1];
        backward[size - 1] = 0;
        for(int i = size - 2; i >= 0; i--){
            max = max < prices[i] ? prices[i] : max;
            backward[i] = backward[i+1] > max - prices[i] ? backward[i+1] : max - prices[i];
        }
        int returnValue = 0;
        for(int i = 0; i < size; i++){
            returnValue = returnValue > forward[i] + backward[i] ? returnValue : forward[i] + backward[i];
        }
        
        return returnValue;
    }
};