class queueE:

    def __init__(self, k):
        self.queue = []
        self.size = k

    def insertTail(self, value):
        if len(self.queue) < self.size:
            self.queue.append(value)
            return value
        return False

    def removeHead(self):
        if self.queue:
            self.queue.pop(0)
        return False

    def geTail(self):

        if len(self.queue) > 0:
            return self.queue[-1]
        return -1

    def getHead(self):

        if len(self.queue) > 0:
            return self.queue[0]
        return -1

    def isFull(self):

        return len(self.queue) == self.size

    def isEmpty(self):

        return len(self.queue) == 0

obj = queueE(9)
print(obj.insertTail(4))







