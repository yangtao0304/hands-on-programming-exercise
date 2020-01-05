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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
