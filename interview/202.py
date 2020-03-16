class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(n):
            res = []
            while n:
                res.append(n % 10)
                n = n//10
            return sum(i*i for i in res)
        if n == 1:
            return True

        slow = next_num(n)
        fast = next_num(slow)
        while slow != fast:
            slow = next_num(slow)
            fast = next_num(fast)
            fast = next_num(fast)
        if slow == 1:
            return True
        return False
