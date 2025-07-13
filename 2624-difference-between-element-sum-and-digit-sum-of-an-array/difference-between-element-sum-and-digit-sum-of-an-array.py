class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        res = []
        add = sum(nums)
        for num in nums:
            if num>9:
                res.extend(int(d) for d in str(num))
            else:
                res.append(num) 
        return abs(sum(nums)-sum(res))        