public class Solution {
    public int hIndex(int[] citations) {
        if(citations == null) return 0;
        Arrays.sort(citations);
        int N = citations.length;
        if(N == 0) return 0;
        int start = 0, end = N;
        int pivot = 0;
        while(start < end){
            pivot = (start + end) / 2;//citations[pivot] is the first paper,which is greater than h(h = N - pivot)
            if(citations[pivot] >= N - pivot && (pivot == 0 || citations[pivot - 1] < N - pivot)){
                return N - pivot;
            }else if(citations[pivot] < N - pivot){
                start++;
            }else{
                end--;
            }
        }
        return N - start;
    }
}