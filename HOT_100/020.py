class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for i in s:
            if i in d:
                stack.append(i)
            else:
                if stack:
                    tmp = stack.pop()
                    if i != d[tmp]:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
