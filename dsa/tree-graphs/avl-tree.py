'''
AVL: Self Balancing Tree invented by GM Adelson-Velsky and EM Landis in 1962
Height Balanced Binary Search Tree

Balance factor of each node should be in between -1 to 1, otherwise it's unbalanced

Balance Factor(k) = height(left(k)) - height(right(k))
Balance Factor = Height of left subtree - Height of right subtree


RR Rotation: AntiClockwise
LL Rotation: clockwise
LR Rotation: AntiClockwise + Clockwise
RL Rotation: Clockwise + AntiClockwise
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def get_height(self, node):
        if not node:
            return 0
        return node.height 
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    
    def insert(self, root, key):
        if not root:
            return Node(key)
        
        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        else:
            return root
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # left left
        if balance > 1 and key < root.left.data:
            return self.right_rotate(root)
        # right right
        if balance < -1 and key > root.right.data:
            return self.left_rotate(root)
        # left right
        if balance > 1 and key > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # right left
        if balance < -1 and key < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def get_min_value_node(self, node):
        current = node
        # Loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        # Standard BST delete
        if not root:
            return root
            
        # If the key to be deleted is smaller than the root's key,
        # then it lies in left subtree
        if key < root.data:
            root.left = self.delete(root.left, key)
            
        # If the key to be deleted is greater than the root's key,
        # then it lies in right subtree
        elif key > root.data:
            root.right = self.delete(root.right, key)
            
        # If key is same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
                
            # Node with two children: Get the inorder successor (smallest
            # in the right subtree)
            temp = self.get_min_value_node(root.right)
            
            # Copy the inorder successor's content to this node
            root.data = temp.data
            
            # Delete the inorder successor
            root.right = self.delete(root.right, temp.data)
        
        # If the tree had only one node then return
        if root is None:
            return root
            
        # Update height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # Get the balance factor
        balance = self.get_balance(root)
        
        # If unbalanced, try the 4 cases
        
        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
            
        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
            
        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
            
        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
            
        return root
        
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data, end=" ")
            self.in_order(root.right)
    def pre_order(self, root):
        if root:
            print(root.data, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)
    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end=" ")

root = None
tree = Node(0)

# Constructing tree given in the above figure
root = tree.insert(root, 21)
root = tree.insert(root, 26)
root = tree.insert(root, 30)
root = tree.insert(root, 9)
root = tree.insert(root, 4)
root = tree.insert(root, 14)
root = tree.insert(root, 25)
root = tree.insert(root, 18)
root = tree.insert(root, 15)
root = tree.insert(root, 10)
root = tree.insert(root, 2)
root = tree.insert(root, 3)
root = tree.insert(root, 7)

# The constructed AVL Tree would be
#        30
#       /  \
#      20   40
#     /  \    \
#    10  25   50

print("Preorder traversal:")
tree.pre_order(root)
print("\nInorder traversal:")
tree.in_order(root)
print("\nPostorder traversal:")
tree.post_order(root)

