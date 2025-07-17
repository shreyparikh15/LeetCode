class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = set()
        ans2 = set()
        n1 = len(nums1)
        n2 = len(nums2)
        for i in range(max(n1, n2)):
            if i<n1 and nums1[i] not in nums2:
                ans1.add(nums1[i])
                
            if i<n2 and nums2[i] not in nums1:
                ans2.add(nums2[i])  
                                 
        return [list(ans1), list(ans2)]  