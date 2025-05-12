from sllnode import sllnode

class sll:
    def __init__(self, head_data = None):
        if head_data:
            self.head = sllnode(head_data)
            self.length = 1
        else:
            self.head = None 
            self.length = 0
        self.curr = self.head

    def __str__(self):
        res = ""
        start = self.head
        while start != None:
            res += f"{start.data} -> "
            start = start.next
        return res 
    
    def __add__(self, other):
        self.curr.next = other.head
        
    def append(self, data):
        new_node = sllnode(data)
        if self.head == None:
            self.head = new_node
            self.curr = new_node 
        else:
            self.curr.next = new_node
            self.curr = self.curr.next
        self.length += 1 

    def insert(self, pos, data):
        if pos < 0  or pos > self.length:
            raise ValueError(f"pos = {pos} can only be positive")
        
        new_node = sllnode(data)
        if pos == 0:
            new_node.next = self.head.next
            if self.curr == self.head.next:
                self.curr = new_node
            self.head = new_node

        elif pos == self.length:
            self.append(data)

        else:
            i = 0
            start = self.head
            while i + 1 < pos:
                start = start.next
                i += 1
            new_node.next = start.next 
            start.next = new_node

        self.length += 1

    def delete_pos(self, pos):
        if pos < 0  or pos > self.length:
            raise ValueError(f"pos = {pos} can only be positive")
        
        if pos == 0:
            self.head = self.head.next
            if self.head == None:
                self.curr = None 

        else:
            i = 0
            start = self.head
            while i + 1 < pos:
                start = start.next
                i += 1
            if pos != self.length - 1:
                start.next = start.next.next
            else:
                start.next = None
                self.curr = start 

        self.length -= 1

    def delete(self, data):
        start = self.head
        i = 0
        while start != None:
            if(start.data == data):
                self.delete_pos(i)
                return
            start = start.next
            i += 1

        raise ValueError(f"data = {self.data} not found in the list")

    def reverse(self):
        prev , curr = None, self.head 
        if curr:
            next = self.head.next 
        else:
            return

        while curr:
            curr.next = prev
            prev = curr 
            curr = next
            if next:
                next = next.next



            


        

