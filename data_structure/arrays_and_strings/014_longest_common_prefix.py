class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        a = self.dict
        for i in word:
            if i not in a:
                a[i] = {}
            a = a[i]
        a['end'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        a = self.dict
        for i in word:
            if i not in a:
                return False
            a = a[i]
        if 'end' in a:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        a = self.dict
        for i in prefix:
            if i not in a:
                return False
            a = a[i]
        return True


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
        t = Trie()
        for i in strs:
            t.insert(i)

        d = t.dict
        res = ''
        while len(d) == 1:
            cur = list(d.keys())[0]
            if cur == 'end':
                break
            res += cur
            d = d[cur]
        return res


if __name__ == "__main__":
    s = Solution()
    strs = ["flower", "flow", "flight"]
    # strs = ['']
    print(s.longest_common_prefix_2(strs))
