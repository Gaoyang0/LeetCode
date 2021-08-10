class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = [[None, False] for _ in range(26)]



    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for ch in word:
            if cur[ord(ch) - ord("a")][0] is None:
                node = [[None, False] for _ in range(26)]
                cur[ord(ch) - ord("a")][0] = node

            cur = cur[ord(ch) - ord("a")][0]
        cur[ord(word[-1]) - ord("a")][1] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        cur = self.root
        for ch in word:
            if cur[ord(ch) - ord("a")][0] is None:
                return False
            else:
                cur = cur[ord(ch) - ord("a")][0]
        return True if cur[ord(word[-1]) - ord("a")][1] else False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for ch in prefix:
            if cur[ord(ch) - ord("a")][0] is None:
                return False
            else:
                cur = cur[ord(ch) - ord("a")][0]
        return True

s = Trie()
print(s.root)
s.insert("ord")
print(s.root)
print(s.search("orde"))