from dllnode import dllnode

class dll:
    def __init__(self, head_data=None):
        if head_data:
            self.head = dllnode(head_data)
            self.length = 1

        else:
            self.head = None
            self.length = 0

        self.curr = self.head

    def __str__(self):
        pass

    def __add__(self):
        pass

    def append(self, data):
        pass  

    def insert(self, pos, data):
        pass 

    def delete_pos(self, pos):
        pass

    def delete(self, data):
        pass

    def reverse(self):
        pass