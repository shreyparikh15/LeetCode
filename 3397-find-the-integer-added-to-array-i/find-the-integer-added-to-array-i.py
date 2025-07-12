class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        count = 0
          
        count = nums2[0]-nums1[0]
        return count
        