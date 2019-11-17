class Solution(object):
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # pythonic implement
        s = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s

    def longest_common_prefix_2(self, strs):
        # 使用字典树查找最长公共前缀
        # 待补充
        # 相关leetcode: 208. 实现 Trie (前缀树)
        # ref: https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/shi-xian-trie-qian-zhui-shu-by-leetcode/
        pass

if __name__ == "__main__":
    s = Solution()
    strs = ["flower", "flow", "flight"]
    print(s.longest_common_prefix(strs))
