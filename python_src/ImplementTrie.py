class TrieNode(object):
    def __init__(self, isWord = False):
        """
        Initialize your data structure here.
        """
        self.isWord = isWord
        self.dc = [None] * 26

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        pivot = self.root
        for c in word:
            index = ord(c) - 97
            if pivot.dc[index] == None:
                node = TrieNode(False)
                pivot.dc[index] = node
            pivot = pivot.dc[index]
        pivot.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        pivot = self.root
        for c in word:
            index = ord(c) - 97
            if pivot.dc[index] == None:
                return False
            pivot = pivot.dc[index]
        return pivot.isWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        pivot = self.root
        for c in prefix:
            index = ord(c) - 97
            if pivot.dc[index] == None:
                return False
            pivot = pivot.dc[index]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")