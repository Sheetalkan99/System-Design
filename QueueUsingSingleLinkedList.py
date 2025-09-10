class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        
        if not self.head:
            return None
        else:
            data = self.head.data
            self.head = self.head.next

        return data
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.data
    
    def display(self):
        if self.head is None:
            print(f"Empty!")
        else:
            temp = self.head
            while temp:
                print(temp.data, end= " " )
                temp = temp.next
            
            

q = Queue()
q.add(1)
q.add(2)
#print(q.peek())
#print(q.remove())
q.display()