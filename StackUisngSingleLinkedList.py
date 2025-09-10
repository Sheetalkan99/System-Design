class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            value = self.top.value
            self.top = self.top.next
            return value
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.value
        
    def print_stack(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next

my_stack = Stack()
my_stack.push(99)
my_stack.push(88)
my_stack.push(77)
my_stack.print_stack()


