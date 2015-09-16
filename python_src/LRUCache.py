class LRUCache(object):
    class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.dic = {}
        self.head = LRUCache.Node(0,0) # insert place
        self.tail = LRUCache.Node(0,0) # remove place
        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, key):
        """
        :rtype: int
        """
        node = self.getNode(key)
        if node: return node.value
        else: return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        node = self.getNode(key)
        if node:
            node.value = value
            return
        self.size += 1
        node = LRUCache.Node(key,value)
        node.right = self.head.right
        node.left = self.head
        post = self.head.right
        post.left = node
        self.head.right = node
        self.dic[key] = node
        if self.size > self.capacity:
            self.size -= 1
            lastNode = self.tail.left
            pre = lastNode.left
            self.tail.left = pre
            pre.right = self.tail
            del self.dic[lastNode.key]



    def getNode(self,key):
        if self.dic.has_key(key):
            node = self.dic[key]
            pre = node.left
            post = node.right
            pre.right = post
            post.left = pre
            node.right = self.head.right
            node.left = self.head
            post = self.head.right
            post.left = node
            self.head.right = node
            return node
        else: return None

