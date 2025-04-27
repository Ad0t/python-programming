'''
Binary Tree Implementation using Arrays
Root
Left child
Right child 
Parent


Advantages:
- Direct Access
- Finding the parent/children is fast

Disadvantages:
- Wastage of memory
- 
'''

class binaryTree():
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def insert(self, value):
        if self.tree[0] is None:
            self.tree[0] = value
        else:
            self._insert(value, 0)

    def _insert(self, value, index):
        if value < self.tree[index]:
            left_child = 2 * index + 1
            if left_child >= self.size:
                return False  # Out of space
            if self.tree[left_child] is None:
                self.tree[left_child] = value
                return True
            return self._insert(value, left_child)
        else:
            right_child = 2 * index + 2
            if right_child >= self.size:
                return False  # Out of space
            if self.tree[right_child] is None:
                self.tree[right_child] = value
                return True
            return self._insert(value, right_child)
    
    def display(self):
        print(self.tree)

    def get_left_child(self, index):
        left_idx = 2 * index + 1
        if left_idx < self.size:
            return left_idx
        return None

    def get_right_child(self, index):
        right_idx = 2 * index + 2
        if right_idx < self.size:
            return right_idx
        return None
    
    def get_parent(self, index):
        if index == 0:
            return None
        return (index - 1)//2

tree = binaryTree(10)
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(1)
tree.insert(4)
tree.insert(7)
tree.insert(9)
tree.display()