class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        n1 = Node(data)
        if self.head == None:
            self.head = n1
        else:
            n1.next = self.head
            self.head = n1

    def pop(self):
        temp = self.head
        self.head = self.head.next
        return temp.data

    def top(self):
        return self.head.data


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())


