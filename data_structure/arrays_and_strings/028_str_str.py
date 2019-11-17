# coding: utf-8
class Solution(object):
    '''
    1. 调用库函数find
    2. 暴力法，O((m-n)n)
    3. KMP
    Other: BF/BM/Sunday
    '''

    def str_str(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        n1 = len(haystack)
        n2 = len(needle)
        if n1 < n2:
            return -1

        def find_idx(idx):
            haystack_p = idx
            needle_p = 0
            while needle_p < n2:
                if haystack[haystack_p] != needle[needle_p]:
                    return False
                else:
                    haystack_p += 1
                    needle_p += 1
            return True

        for i in range(n1-n2+1):
            if find_idx(i):
                return i
        return -1

    def str_str_2(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

    def str_str_3(self, haystack, needle):
        '''
        kmp算法
        '''
        # 待补充
        # ref：http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
        pass
