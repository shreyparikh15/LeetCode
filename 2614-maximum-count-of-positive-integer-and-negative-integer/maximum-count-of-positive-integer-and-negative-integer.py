class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_pos = 0
        count_neg = 0
        for i in range(len(nums)):
            if nums[i]>0:
                count_pos +=1
            elif nums[i]<0: 
                count_neg +=1
                
        if count_pos>count_neg:
            return count_pos
        else:
            return count_neg              