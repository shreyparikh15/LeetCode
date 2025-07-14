class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for key in freq:
            if freq[key]>len(nums)//2:
                return key