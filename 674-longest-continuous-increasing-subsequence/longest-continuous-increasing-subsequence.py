class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n =len(nums)
        if not nums:
            return 0
        maxi = 1
        cnt  = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                cnt += 1
                maxi = max(maxi,cnt)
            else:
                cnt = 1
        return maxi
            
        


            
        