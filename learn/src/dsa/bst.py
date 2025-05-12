from btnode import btnode

class bst:
    def __init__(self, root_data):
        if root_data:
            self.root = btnode(root_data)
            self.num_nodes += 1

        else:
            self.root = None 
            self.num_nodes = 0

        self.height = 0
        self.curr = self.root 

    def __str__(self):
        return f"bst[root={self.root}, number_of_nodes={self.num_nodes}, height={self.height}]"
    
    def insert(self, node_data):
        self.root = self._insert_recurisve(self.root, node_data)

    def _insert_recurisve(self, root ,node_data):
        if not root:
            return btnode(node_data)
        
        if node_data <= root.data:
            return self._insert_recurisve(root.left, node_data)
        
        if node_data > root.data:
            return self._insert_recurisve(root.right, node_data)

        return root
    
    def left_most_node_data(self, root):
        while root.left:
            root = root.left 
            if not root.left:
                return root.data

    def delete(self, node_data):
        self.root = self._delete_recursive(self.root, node_data)

    def _delete_recursive(self, root, node_data):
        if root.data == node_data:
            if root.left == None and root.right == None:
                return None 
            
            if root.left == None or root.right == None:
                return root.left if root.left else root.right 
            
            else:
                root.data = self.left_most_node_data(root.right)
                self._delete_recursive(root.right, root.data)

        elif node_data  < root.data:
            return self._delete_recursive(root.left, node_data)
        
        elif node_data > root.data:
            return self._delete_recursive(root.right, node_data)
        
        return root 


    def inorder(self):
        return self._inorder_recursive(self.root, )

    def _inorder_recursive(self, root, res):
        if not root:
            return
        self._inorder_recursive(root.left, res)
        res.append(root.data)
        self._insert_recurisve(root.right, res)

        
    def preorder(self):
        return self._inorder_recursive(self.root, [])
    
    def _preorder_recursive(self, root, res):
        if not root:
            return
        res.append(root.data)
        self._preorder_recursive(root.left, res)
        self._preorder_recursive(root.right, res)

    def postorder(self):
        return self._postorder_recursive(self.root, [])

    def _postorder_recursive(self, root, res):
        if not root:
            return
        self._postorder_recursive(root.left, res)
        self._postorder_recursive(root.right, res)
        res.append(root.data)

    def height(self):
        return self._height_recursive(self.root)
    
    def _height_recursive(self, root):
        if not root:
            return 0
        return 1 + max(self._height_recursive(root.left), self._height_recursive(root.right))

    


