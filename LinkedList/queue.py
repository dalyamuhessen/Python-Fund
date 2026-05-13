class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def peek(self):
        if not self.items:
            return None
        return self.items[0]
q = Queue()
print(q.dequeue())  
q.enqueue(10)
q.enqueue(200)
q.enqueue(39)
print(q.items)      

 