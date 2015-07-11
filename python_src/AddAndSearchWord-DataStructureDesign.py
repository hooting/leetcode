#each node can have at most 26 child which is stored by dict
#the key,value pair in dict is (character,node)
class WordDictionary:
    class Node:
        def __init__(self,val=None):
            self.val = val
            self.next = dict()

    # initialize your data structure here.
    def __init__(self):
        self.head = self.Node()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        candidates = self.head.next
        for c in word:
            if candidates.has_key(c):
                candidates = candidates[c].next
            else:
                node = self.Node(c)
                candidates[c] = node
                candidates = node.next
        candidates[None] = None



    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        candidates = self.head.next
        return self.recursive(word,candidates,0)

    def recursive(self,word,candidates,pos):
        if pos == len(word):
            if candidates.has_key(None): return True
            else: return False
        if word[pos] == '.':
            for node in candidates.values():
                if node == None:continue
                if self.recursive(word,node.next,pos + 1): return True
        else:
            if not candidates.has_key(word[pos]): return False
            return self.recursive(word,candidates[word[pos]].next,pos+1)
        return False



# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")