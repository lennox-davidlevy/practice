class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def traverse_list(self, callback):
        if self.get_size() == 0:
            print("List empty")
            return
        current = self.head
        while current:
            callback(current.data)
            current = current.next

    def _insert_in_empty_list(self, data):
        new_node = Node(data)
        self.head = new_node
        self.size += 1
        return

    def insert_at_start(self, data):
        if self.get_size() == 0:
            self._insert_in_empty_list(data)
            return
        new_node = Node(data)
        current = self.head
        current.prev = new_node
        new_node.next = current
        self.size += 1
        return

    def insert_at_end(self, data):
        if self.get_size() == 0:
            self._insert_in_empty_list(data)
            return
        current = self.head
        while current.next:
            current = current.next
        new_node = Node(data)
        current.next = new_node
        new_node.prev = current
        self.size += 1
        return

    def insert_after_key(self, key, data):
        if self.get_size() == 0:
            print("List is empty")
            return
        current = self.head
        new_node = Node(data)
        while current:
            if current.data == key:
                new_node.next = current.next
                current.next = new_node
                self.size += 1
                return
            current = current.next
        print("Key does not exist, nothing inserted")
        return

    def insert_before_key(self, key, data):
        if self.get_size() == 0:
            print("List empty, nothing inserted")
            return
        current = self.head
        new_node = Node(data)
        while current:
            if current.data == key:
                new_node.prev = current.prev
                current.prev = new_node
                new_node.next = current
                return
            current = current.next
        print("Key not in list, nothing inserted")
        return


d_list = DoublyLinkedList()
d_list.insert_at_start(10)
d_list.insert_at_end(11)
d_list.insert_after_key(11, "hello")
d_list.insert_before_key(11, "goodbye")
d_list.traverse_list(print)
