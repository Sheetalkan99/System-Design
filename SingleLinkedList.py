class Node:
    "Class to represnt a node in linkedlist."
    def __init__(self,data):
        self.data = data 
        self.next = None
class Linkedlist:
    "represnt singly linkedlist"
    def __init__(self):
        self.head = None
    
    def add(self, data):
        "Add a new node at end"
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next 
        current.next = new_node

    def remove(self,key):
        "Remove node"
        current = self.head
        prev = Node
        
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Key {key} not in the list.")
        
        if not prev:
            self.head = current.next
        else:
            prev.next = current.next
        print(f"Node with data {key} removed.")

    def display(self):
        current = self.head
        if not current:
            print("Empty")
            return 
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self,position):
        if position < 0:
            print("Negative")
            return
        
        current = self.head
        prev = None
        index = 0

        while current and index != position:
            prev = current
            current = current.next
            index += 1

        if not current:
            print("Posotion out of range")
            return
        if not prev:
            self.head = current.next
        else:
            prev.next = current.next
            print (f"Node at position {position} deleted.")


# Interactive menu
if __name__ == "__main__":
    ll = Linkedlist()

    while True:
        print("\nChoose an option:")
        print("1. Add element")
        print("2. Remove element")
        print("3. Delete element at a position")
        print("4. Display linked list")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            data = input("Enter the value to add: ")
            ll.add(data)
        elif choice == "2":
            key = input("Enter the value to remove: ")
            ll.remove(key)
        elif choice == "3":
            position = int(input("Enter the position to delete: "))
            ll.delete(position)
        elif choice == "4":
            print("Current linked list:")
            ll.display()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")