class MyStack:
    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)
        
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.pop(0))

    def pop(self):
        return self.q.pop(0)

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0
        
s = MyStack()
s.push(1)
s.push(2)
s.push(3)

print(s.top())
print(s.pop())
print(s.pop())
print(s.empty())

