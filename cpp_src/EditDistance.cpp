/**
 * reference to https://leetcode.com/discuss/10426/my-o-mn-time-and-o-n-space-solution-using-dp-with-explanation
 * Use f[i][j] to represent the shortest edit distance between word1[0,i) and word2[0, j). Then compare the last character of
 * word1[0,i) and word2[0,j), which are c and d respectively (c == word1[i-1], d == word2[j-1]):
 * if c == d, then : f[i][j] = f[i-1][j-1]
 * Otherwise we can use three operations to convert word1 to word2:
 * (a) if we replaced c with d: f[i][j] = f[i-1][j-1] + 1;
 * (b) if we added d after c: f[i][j] = f[i][j-1] + 1;
 * (c) if we deleted c: f[i][j] = f[i-1][j] + 1;
 * 
 */
class Solution {
public:
    int minDistance(string word1, string word2) {
        int size1 = word1.size();
        int size2 = word2.size();
        int** ary = new int*[size1 + 1];
        for(int i = 0; i <= size1; ++i)
            ary[i] = new int[size2 + 1];
        for(int i = 0; i <= size2; i++)
            ary[0][i] = i;
        for(int i = 0; i <= size1; i++)
            ary[i][0] = i;
        for(int i = 1; i <= size1; i++){
            for(int j = 1; j <= size2; j++){
                if(word1[i-1] == word2[j-1]){
                    ary[i][j] = ary[i-1][j-1];
                }else{
                    ary[i][j] = getMin(ary[i-1][j-1],ary[i-1][j],ary[i][j-1]) + 1;
                }
            }
        }
        int result = ary[size1][size2];
        for(int i = 0; i <= size1; ++i)
            delete [] ary[i];
        delete [] ary;
        return result;
    }
    
    int getMin(int a,int b,int c){
        int m = a > b ? b : a;
        m = m > c ? c : m;
        return m;
    }
};