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
        
        # ref：http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html

        # ps: leetcode测试超时 = =、
        
        if not needle:
            return 0

        def get_partial_matching_value(p):
            res = []
            for i in range(len(p)):
                sub_p = p[:i+1]
                value = 0
                for j in range(len(sub_p)):
                    if sub_p[:j] == sub_p[-j:]:
                        value = max(value, len(sub_p[:j]))
                res.append(value)
            return res

        partial_matching_value = get_partial_matching_value(needle)

        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                # 已匹配字符数：j
                j = partial_matching_value[j-1]
        
        if j==len(needle):
            return i-j
        return -1


if __name__ == "__main__":
    t = 'BBC ABCDAB ABCDABCDABDE'
    p = 'ABCDABD'
    s = Solution()
    print(s.str_str_3(t,p))
