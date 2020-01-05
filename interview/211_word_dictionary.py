class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        t = self.d
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['end'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # 匹配时，遇到.就进行深搜
        cut = False

        def f(td, s):  # 深搜，参数为：当前子字典，当前串
            nonlocal cut
            if cut:  # 剪枝
                return True
            t = td
            for i, c in enumerate(s):
                if c == '.':
                    # 深搜扩展
                    return sum(f(t[j], s[i + 1:]) for j in t if j != 'end')
                if c not in t:
                    return False
                t = t[c]
            cut = 'end' in t
            return cut
        return f(self.d, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
