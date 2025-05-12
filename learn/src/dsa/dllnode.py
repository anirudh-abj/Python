class dllnode:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self):
        return f"dllnode[data={self.data}]"