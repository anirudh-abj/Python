from bst import bst
from btnode import btnode

class avl(bst):
    def __init__(self):
        super.__init__()

    def __str__(self):
        pass

    def insert(self, node_data):
        self._insert_recurisve(self, self.root, node_data)
        self.balance()

    def delete(self, node_data):
        self._delete_recursive(self, self.root, node_data)
        self.balance()

    def left_rotate(self, parent, child):
        temp = child.left
        child.left = parent
        parent.right = temp

    def right_rotate(self, parent, child):
        temp = child.right
        child.right = parent
        parent.left = temp

    def is_balanced(self):
        pass 

    def balance(self):
        pass 

    
