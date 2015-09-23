class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2,nums1)
        len1 = len(nums1)
        len2 = len(nums2)
        start = 0
        end = len1
        mid1 = mid2 = 0
        while start <= end:
            i = (start + end) / 2
            j = (len1 + len2 - 2 * i + 1) / 2
            if i < len1 and j > 0 and nums2[j-1] > nums1[i]: start = i + 1
            elif j < len2 and i > 0 and nums1[i-1] > nums2[j]: end = i - 1
            else:
                if i == 0:
                    mid1 = nums2[j-1]
                elif j == 0:
                    mid1 = nums1[i-1]
                else:
                    mid1 = max(nums1[i-1],nums2[j-1])
                break
        if(len1 + len2) % 2 == 1: return mid1
        if i == len1: mid2 = nums2[j]
        elif j == len2: mid2 = nums1[i]
        else: mid2 = min(nums2[j],nums1[i])
        return (mid1 + mid2) / 2.0
                    
            