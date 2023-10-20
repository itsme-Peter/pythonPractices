# linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        # print(type(new_node))
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.nect
            current.next = new_node

    def read(self):
        current = self.head
        lst = []
        while current:
            # print(current.data)
            lst.append(current.data)
            current = current.next
        print(lst)

    def update(self,data,target):
        current = self.head
        while current:
            if current.data == target:
                current.data = data
                return
            current = current.next
        else:
            print(f"{target} not found in linked list")

    def delete(self,data):
        if not self.head:
            return
        
        current = self.head
        if current.data == data:
            self.head = current.next
        
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

linked = linkedList()
linked.append(10)
linked.append(14)
linked.update(15,14)
linked.delete(15)
linked.read()
