class Solution(object):
    def minOperations(self, nums):
        ope = 0
        n  = len(nums)
        for i in range(n-2):
          if nums[i] == 0:
            nums[i] ^= 1
            nums[i + 1] ^= 1
            nums[i + 2] ^= 1
            ope +=1
        if all(x == 1 for x in nums):
            return ope
                
        return -1