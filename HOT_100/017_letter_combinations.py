# 递归的方法相当于深度遍历，队列的方法相当于广度遍历

# 这个分析比较好理解：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/tong-su-yi-dong-dong-hua-yan-shi-17-dian-hua-hao-m/


class Solution:
    # 回溯
    '''
    回溯是一种通过穷举所有可能情况来找到所有解的算法
    如果一个候选解最后被发现并不是可行解，回溯算法会舍弃它，并在前面的一些步骤做出一些修改，并重新尝试找到可行解
    '''
    # 循环 + 递归

    def letterCombinations(self, digits):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination+letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output

    def letterCombinations2(self, digits):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        if not digits:
            return []

        res = [""]

        for i in digits:
            next_res = []
            for letter in phone[i]:
                for tmp in res:
                    next_res.append(tmp+letter)
            res = next_res
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations2('23'))
