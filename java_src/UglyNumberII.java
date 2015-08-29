/**
 * candidates[0] stores data which to * 2
 * candidates[1] stores data which to * 3
 * candidates[2] stores data which to * 5
 * each time, we fetch the smallest value among candidates[0][0] * 2, candidates[1][0] * 3, candidates[2][0] * 5
 * and put the smallest value to the tail of these three list
 * we may meet the same value like 2 * 3, and 3 * 2, thus we need preValue to record the last value.
 */
public class Solution {
    public int nthUglyNumber(int n) {
        if(n <= 0) return -1;
        List<Integer>[] candidates = new ArrayList[3];
        for(int i = 0; i < 3; i++){
            candidates[i] = new ArrayList<Integer>();
            candidates[i].add(1);
        }
        int num = 1;
        int value = 1;
        int preValue = -1;
        Map<Integer,Integer> factors = new HashMap<Integer,Integer>();
        factors.put(0,2);
        factors.put(1,3);
        factors.put(2,5);
        while(num < n){
            int minIndex = minValueIndex(candidates[0].get(0),candidates[1].get(0),candidates[2].get(0));
            value = candidates[minIndex].get(0) * factors.get(minIndex);
            candidates[minIndex].remove(0);
            if(preValue != value){
                for(int i = 0; i < 3; i++){
                    candidates[i].add(value);
                }
                num +=1;
            }
            preValue = value;
        }
        return value;
        
    }
    
    private int minValueIndex(int a1,int a2,int a3){
        if(a1 * 2 <= a2 * 3 && a1 * 2 <= a3 * 5) return 0;
        else if(a2 * 3 <= a1 * 2 && a2 * 3 <= a3 * 5) return 1;
        else return 2;
    }
}