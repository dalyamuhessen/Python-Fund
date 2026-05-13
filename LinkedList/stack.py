class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

s = Stack()
print(s.pop())     
s.push(20)
s.push(30)
print(s.items)     
print(s.peek())    
print(s.pop())     
print(s.items)    