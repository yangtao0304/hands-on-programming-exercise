class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.strip().split()
        return ' '.join(reversed(list_s))
