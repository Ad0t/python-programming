'''
Advantages:
- Wastage of Memory
- Insertion and deletion will be easy

Disadvantages:
- Does not provide direct access
- Addtional space in each node

Expression: Infix, Prefix(Polish notation), Postfix(Reverse Polish notation)
Preorder Traversal
- To traverse a nonempty binary tree
    1. Visit the root
    2. If the left subtree is nonempty, do a preorder traversal on it
    3. If the right subtree is nonempty, do a preorder traversal on it
Postorder Traversal
- To traverse a nonempty binary tree
    1. If the left subtree is nonempty, do a postorder traversal on it
    2. If the right subtree is nonempty, do a postorder traversal on it
    3. Visit the root
Inorder Traversal
- To traverse a nonempty binary tree
    1. If the left subtree is nonempty, do a inorder traversal on it
    2. Visit the root
    3. If the right subtree is nonempty, do a intorder traversal on it
'''

'''
WAP to convert infix expression into postfix
'''

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class binaryTree:
    def __init__(self):
        self.root = None

    def insertNode(self, root, key):
        if root is None:
            return Node(key)
        if root.val == key:
                return root
        if root.val < key:
                root.right = self.insertNode(root.right, key)
        else:
                root.left = self.insertNode(root.left, key)
        return root
        
    