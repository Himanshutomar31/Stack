class Stack:
    def __init__(self):
        self.top = -1
        self.max = 10
        self.lst = list()

    def push(self, data):
        if (self.top + 1 > self.max):
            return ("Stack Overflow")
        else:
            self.top += 1
            self.lst.append(data)

    def pop(self):
        if self.top == -1:
            return ("Stack Underflow")
        temp = self.lst[self.top]
        self.top -= 1
        return temp

    def top(self):
        if self.top == -1:
            return ("Stack Underflow")
        return self.lst[self.top]

    def is_full(self):
        if self.top == self.max:
            return True
        return False

    def is_empty(self):
        if self.top == -1:
            return True
        return False


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())


