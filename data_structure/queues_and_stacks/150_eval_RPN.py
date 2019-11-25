class Solution(object):
    '''
    (a+b)*c-(a+b)/e
    →((a+b)*c)((a+b)/e)-
    →((a+b)c*)((a+b)e/)-
    →(ab+c*)(ab+e/)-
    →ab+c*ab+e/-
    '''
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        valid_ops = {'+', '-', '*', '/'}
        stack = []

        for i in tokens:
            if i not in valid_ops:
                stack.append(i)
            else:
                value_2 = int(stack.pop())
                value_1 = int(stack.pop())
                if i == '+':
                    stack.append(value_1+value_2)
                elif i == '-':
                    stack.append(value_1-value_2)
                elif i == '*':
                    stack.append(value_1*value_2)
                elif i == '/':
                    stack.append(int(value_1/value_2))

        return stack[-1]


if __name__ == "__main__":
    s = Solution()
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    print(s.evalRPN(tokens))
