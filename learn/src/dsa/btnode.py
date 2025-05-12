class btnode:
    def __init__(self, data):
        self.lchild = None 
        self.data = data
        self.rchild = None

    def __str__(self):
        return f"btnode[data={self.data}]"