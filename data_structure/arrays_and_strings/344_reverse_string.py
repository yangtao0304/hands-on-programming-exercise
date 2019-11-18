class Solution(object):
    def reverse_string(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        p_head = 0
        p_tail = len(s)-1
        while p_head < p_tail:
            s[p_head], s[p_tail] = s[p_tail], s[p_head]
            p_head += 1
            p_tail -= 1
