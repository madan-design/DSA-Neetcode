class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = nums.count(0)
        res = []
        for num in nums:
            if num!=0:
                prod*=num
        if zeros > 1:
            return res[0]*len(nums)
        elif zeros ==1:
            for num in nums:
                res.append(prod if num ==0 else 0)
            return res
        else:
            for num in nums:
                num = prod//num
                res.append(num)
            return res
                        