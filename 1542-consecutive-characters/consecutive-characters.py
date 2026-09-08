class Solution(object):
    def maxPower(self, s):
        maxi = 1
        cnt = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cnt +=1
                maxi = max(maxi,cnt)
            else:
                cnt =1
        return maxi
        
        