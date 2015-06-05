/**
 * reference to https://leetcode.com/discuss/15790/share-my-o-log-min-m-n-solution-with-explanation
 * Put A's left part and B's left part into one set. (Let's name this set "LeftPart")
 * Put A's right part and B's right part into one set. (Let's name this set"RightPart")
 *             LeftPart           |            RightPart 
 * { A[0], A[1], ... , A[i - 1] } | { A[i], A[i + 1], ... , A[m - 1] }
 * { B[0], B[1], ... , B[j - 1] } | { B[j], B[j + 1], ... , B[n - 1] }
 * so, we only need to ensure two conditions:
 * 1) LeftPart's length == RightPart's length (or RightPart's length + 1)
 * 2) All elements in RightPart is greater than elements in LeftPart.
 *To ensure these two condition, we just need to ensure:
 * (1) i + j == m - i + n - j (or: m - i + n - j + 1)
 *  if n >= m, we just need to set: 
 *      i = 0 ~ m, j = (m + n + 1) / 2 - i
 * (2) B[j - 1] <= A[i] and A[i - 1] <= B[j]
 *  considering edge values, we need to ensure:
 *  (j == 0 or i == m or B[j - 1] <= A[i]) and (i == 0 or j == n or A[i - 1] <= B[j])
 */
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        if (m > n) return findMedianSortedArrays(nums2,nums1);
        int minidx = 0, maxidx = m;
        int i, j;//i stands for there are i numbers of nums1 in the left of merged array, and j corresponds to nums2
        int num1,num2;//num1 and num2 stands the middle number of tthe merged array;
        int mid = (m + n + 1) >> 1;
        while (minidx <= maxidx){
            i = (minidx + maxidx) >> 1;
            j = mid - i;
            if (i<m && j>0 && nums2[j-1] > nums1[i]) minidx = i + 1;
            else if (i>0 && j<n && nums2[j] < nums1[i-1]) maxidx = i - 1;
            else{
                if (i == 0) num1 = nums2[j-1];
                else if (j == 0) num1 = nums1[i - 1];
                else num1 = max(nums1[i-1],nums2[j-1]);
                break;
            }
        }
        if (((m + n) & 1)) return num1;
        if (i == m) num2 = nums2[j];
        else if (j == n) num2 = nums1[i];
        else num2 = min(nums1[i],nums2[j]);
        return (num1 + num2) / 2.;
    }
};