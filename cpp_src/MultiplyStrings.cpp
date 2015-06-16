class Solution {
public:
    string multiply(string num1, string num2) {
        int size1 = num1.size();
        int size2 = num2.size();
        int size = size1 + size2;
        if(size == 0) return "0";
        vector<int> vect1(size1,0);
        vector<int> vect2(size2,0);
        for(int i = 0; i < size1; i++){
            vect1[size1 - 1 -i] = num1[i] - '0';
        }
        for(int i = 0; i < size2; i++){
            vect2[size2 - 1 - i] = num2[i] - '0';
        }
        vector<int> nums(size,0);
        for(int i = 0; i < size1; i++){
            for(int j = 0; j < size2; j++){
                int value = vect1[i] * vect2[j];
                nums[i + j] += value % 10;
                nums[i + j + 1] += value / 10;
            }
        }
        for(int i = 0; i < size - 1; i++){
            if(nums[i] >= 10){
                nums[i + 1] += nums[i] / 10;
                nums[i] %= 10;
            }
        }
        string result;
        int index = size - 1;
        while(nums[index] == 0 && index > 0) index--;
        for(int i = index; i >= 0; i--){
            result.append(1,nums[i] + '0');
        }
        return result;
    }
};