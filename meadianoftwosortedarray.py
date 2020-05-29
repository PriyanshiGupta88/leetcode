class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        l=len(nums)
        if(l%2!=0):
            return(nums[(l//2)])
        else:
            k=(nums[(l//2)]+nums[(l//2)-1])/2
            return k
