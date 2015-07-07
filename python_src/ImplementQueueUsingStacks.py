class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        ret = self.queue[0]
        del self.queue[0]
        return ret
        

    # @return an integer
    def peek(self):
        return self.queue[0]
        

    # @return an boolean
    def empty(self):
        return len(self.queue) == 0
        