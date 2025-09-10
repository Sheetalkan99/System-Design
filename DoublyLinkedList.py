class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DLinkedlist:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def remove(self,key):
        current = self.head

        while current and current.data != key:
            current = current.next

        if not current:
            print(f"Key {key} nit found!")
            return 
        
        if not current.prev:
            self.head = current.next
            if self.head:
                self.head.prev = None
        else:
            current.prec.next = current.next 
            if current.next:
                current.next.prev = current.prev
        print(f"Node with data {key} removed.")

    def display_forward(self):
        current = self.head
        if not current:
            print("Empty")
            return 
        while current:
            print(current.data, end = " <->")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        if not current:
            print("Empty.")
            return
        
        while current.next:
            current = current.next

        while current:
            print(current.data, end = "<->")
            current = current.prev
        print("None")


    def delete(self, position):
        if position < 0:
            print("Position Non-Negative Integer.")
            return
        
        current = self.head
        index = 0

        while current and index != position:
            current = current.next
            index += 1

        if not current:
            print("Position out of range.")
            return 
        
        if not current.prev:
            self.head = current.next
            if self.head:
                self.head.prev = None
        else:
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev

        print(f"Node at position {position} deleted.")

# Interactive menu
if __name__ == "__main__":
    dll = DLinkedlist()

    while True:
        print("\nChoose an option:")
        print("1. Add element")
        print("2. Remove element")
        print("3. Delete element at a position")
        print("4. Display forward")
        print("5. Display backward")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            data = input("Enter the value to add: ")
            dll.add(data)
        elif choice == "2":
            key = input("Enter the value to remove: ")
            dll.remove(key)
        elif choice == "3":
            position = int(input("Enter the position to delete: "))
            dll.delete(position)
        elif choice == "4":
            print("Linked list (forward):")
            dll.display_forward()
        elif choice == "5":
            print("Linked list (backward):")
            dll.display_backward()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")