class Queue: 
    def __init__ (self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def inQueue (self, item):
        self.items.insert(0, item)

    def outQueue (self):
        return self.intems.pop()

    def size (self):
        return len(self.items)

    def printQueue (self):
        for items in self.items:
            print (items, ",", end = '')

q=Queue()

print (q.isEmpty())

q.inQueue(1)

q.inQueue(2)

q.inQueue(3)

print (q.isEmpty())

q.printQueue()