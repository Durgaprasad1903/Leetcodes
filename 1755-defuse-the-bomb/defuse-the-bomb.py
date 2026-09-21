class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        if k > 0:
            left = 1
            right = k
        else:
            left = n + k
            right = n - 1
        window_sum  = 0
        for i in range(left,right + 1):
            window_sum += code[i % n]
        for i in range(n):
            res[i] = window_sum
            window_sum -= code[left % n]
            left += 1
            right += 1
            window_sum += code[right % n]
        return res

        
         