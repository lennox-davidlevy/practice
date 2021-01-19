class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def _is_empty(self):
        return self.get_size() == 0

    def prepend(self, val):
        new_node = Node(val)
        current = self.head
        new_node.next = self.head
        if self.head == None:
            new_node.next = new_node

        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node
        self.size += 1

    def append(self, val):
        if self._is_empty():
            self.head = Node(val)
            self.head.next = self.head
            self.size += 1
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node = Node(val)
        current.next = new_node
        new_node.next = self.head
        self.size += 1
        return

    def traverse(self, callback):
        if self._is_empty():
            print("List is empty")
            return
        current = self.head
        while current:
            callback(current.data)
            current = current.next
            if current == self.head:
                break
        return


c_list = CircularLinkedList()
c_list.prepend("start")
# c_list.append("third from end")
# c_list.append("second from end")
c_list.append("end")
c_list.traverse(print)
