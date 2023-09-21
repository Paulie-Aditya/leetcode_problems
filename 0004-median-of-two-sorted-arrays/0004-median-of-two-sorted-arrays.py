class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = sorted(nums1 + nums2)
        if (len(x))%2 != 0:
            return x[len(x)//2]
        else:
            return float((x[int(len(x)//2)] + x [int((len(x)//2)-1)]))/2
            