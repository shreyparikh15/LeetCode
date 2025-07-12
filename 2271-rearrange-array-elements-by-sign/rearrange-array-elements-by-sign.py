class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in range(0, len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])    
        num = pos+neg
        #return num
        res = []
        for i in range(0,len(pos)):
            res.append(pos[i])
            #i+=1
            res.append(neg[i])
        return res    