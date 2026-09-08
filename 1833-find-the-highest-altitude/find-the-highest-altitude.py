class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maxi = 0
        curr = 0
        n = len(gain)
        for i in range(n):
            curr += gain[i]
            maxi = max(maxi,curr)
            
        return maxi
        