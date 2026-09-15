class Solution(object):
    def isValid(self, s):
        stack = []
        mapp = {")":"(","}":"{","]":"["}
        for char in s:
            if char in mapp:
                top_ele = stack.pop() if stack else "#"
                if mapp[char] != top_ele:
                    return False
            else:
                    stack.append(char)
        return not stack
        
        