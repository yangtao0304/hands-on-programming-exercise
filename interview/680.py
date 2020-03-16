class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(s):
            left = 0
            right = len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s)-1
        a, b = None, None
        while left < right:
            if s[left] != s[right]:
                a = left
                b = right
                break
            left += 1
            right -= 1

        if a == None:
            return True
        else:
            return valid(s[left:right]) or valid(s[left+1:right+1])
