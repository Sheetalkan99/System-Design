from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def display(self):
        import json

        def node_to_dict(node):
            if node is None:
                return None
            return {
                "val": node.val,
                "left": node_to_dict(node.left),
                "right": node_to_dict(node.right),
            }

        print(json.dumps(node_to_dict(self.root), indent=2))

    def insertn(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return self

        temp = self.root
        while True:
            if new_node.val == temp.val:
                return None  # Duplicate values are not allowed

            if new_node.val < temp.val:
                if temp.left is None:
                    temp.left = new_node
                    return self
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return self
                temp = temp.right

    def find(self,val):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if val < temp.val:
                temp = temp.right
            if val > temp.val:
                temp = temp.right
            else: 
                return True
        return False
    
    def bfs(self):
            if self.root is None:
                return []
            
            queue = deque([self.root])
            result = []

            while queue:
                current = queue.popleft()  # Dequeue (FIFO)
                result.append(current.val)  # Process node
                
                if current.left:
                    queue.append(current.left)  # Enqueue left child
                if current.right:
                    queue.append(current.right)  # Enqueue right child
            
            return result


# Example usage
first = BST()
first.insertn(10)
first.insertn(22)
first.display()
print(first.find(22))
print("BFS Traversal:", first.bfs()) 