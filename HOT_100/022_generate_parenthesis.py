'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    # 暴力法
    def generateParenthesis(self, n):
        def generate(A, n):
            if n == 0:
                if valid(A):
                    ans.append(''.join(A))
            else:
                for i in ['(', ')']:
                    generate(A+i, n-1)

        # 利用左括号的数量减去右括号的数量的差值判断是否有效
        def valid(A):
            bal = 0
            for i in A:
                if i == '(':
                    bal += 1
                else:
                    bal -= 1
                # 这一个判断容易忽略掉
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate('', 2*n)
        return ans

    # 不像方法一一样每次添加，而是在知道序列仍然保持有效的时候才添加
    # n个左括号，n个右括号，判断：若左括号数小于n，可以加左括号，若右括号数小于左括号数，可以加右括号

    def generateParenthesis2(self, n):
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2*n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack('', 0, 0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
