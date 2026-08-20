class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combine=nums1+nums2
        combine.sort()
        total = len(combine)
        if total %2 != 0:
            ans = ((total+1)//2)-1
            return combine[ans]
        else:
            a = (total//2)-1
            b = a+1
            ans = ((combine[a]) + (combine[b]))/2
            return ans
