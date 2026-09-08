class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxi = max(candies)
        n = len(candies)
        arr = [] * n
        for i in range(n):
            if candies[i] + extraCandies >= maxi:
                arr.append(bool(1))
            else:
                arr.append(bool(0))
                
        return arr
        