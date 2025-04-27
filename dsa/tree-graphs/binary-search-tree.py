'''
Binary Search Tree
Left child < root
Right child > root
'''

'''
1,2,4, 6, 8,  9,15,29
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def insertNode(root, key):
    if root == None:
        return TreeNode(key)
    else:
        if root.data < key:
            root.right = insertNode(root.right, key)
        else:
            root.left = insertNode(root.left, key)
    return root

def inorder(root):
    if root == None:
        return
    else:
        inorder(root.left)
        print(f"|{root.data}|", end=" ")
        inorder(root.right)
        return
def preorder(root):
    if root == None:
        return
    else:
        print(f"|{root.data}|", end=" ")
        preorder(root.left)
        preorder(root.right)
        return
def postorder(root):
    if root == None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(f"|{root.data}|", end=" ")
        return

if __name__ == "__main__":
    root = TreeNode(9)
    insertNode(root, 7)
    insertNode(root, 11)
    insertNode(root, 10)
    insertNode(root, 8)
    insertNode(root, 6)
    insertNode(root, 12)
    # root.left = TreeNode(7)
    # root.right = TreeNode(11)
    # root.left.left = TreeNode(6)
    # root.left.right = TreeNode(8)
    # root.right.left = TreeNode(10)
    # root.right.right = TreeNode(12)

    print("\nIn Order Traversal:", end="\n")
    inorder(root)
    print("\nPre Order Traversal:", end="\n")
    preorder(root)
    print("\nPost Order Traversal:", end="\n")
    postorder(root)
    