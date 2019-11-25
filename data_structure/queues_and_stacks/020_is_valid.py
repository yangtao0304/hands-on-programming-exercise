class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match_dict = {'(': ')',
                      '[': ']',
                      '{': '}'}
        stack = []
        for char in s:
            if char in match_dict.keys():
                stack.append(char)
            else:
                if stack and char == match_dict[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return not stack
        # if stack:
        #     return False
        # return True

    def is_valid_2(self, s):
        stack = []
        match_dict = {')': '(',
                      ']': '[',
                      '}': '{'}
        for char in s:
            if char in match_dict:
                ele_top = stack.pop() if stack else '#'
                if ele_top != match_dict[char]:
                    return False
            else:
                stack.append(char)

        return not stack
