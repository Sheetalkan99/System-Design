# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val: int):
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)
        

def build_test_tree():
    # Creating the tree
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    node7 = TreeNode(7)
    root = TreeNode(4, node2, node7)
    return root

# Test function
def test_searchBST():
    solution = Solution()
    root = build_test_tree()

    result = solution.searchBST(root, 2)
    print(f"Found Node: {result.val if result else 'None'}")  # Should print 2

    result = solution.searchBST(root, 5)
    print(f"Found Node: {result.val if result else 'None'}")  # Should print None

test_searchBST()
