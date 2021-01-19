class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def _is_empty(self):
        return self.get_size() == 0

    def _insert_empty_list(self, val):
        new_node = Node(val)
        self.head = new_node
        self.size += 1
        return

    def add_node_to_start(self, val):
        if self._is_empty():
            self._insert_empty_list(val)
            return
        new_node = Node(val)
        current = self.head
        current.prev = new_node
        new_node.next = current
        self.head = new_node
        self.size += 1
        return

    def add_node_to_end(self, val):
        if self._is_empty():
            self._insert_empty_list(val)
            return
        current = self.head
        while current.next:
            current = current.next
        new_node = Node(val)
        new_node.prev = current
        current.next = new_node
        self.size += 1
        return

    def add_after_key(self, key, val):
        if self._is_empty():
            print("List empty, nothing added")
            return
        current = self.head
        new_node = Node(val)
        while current:
            if current.data == key:
                new_node.next = current.next
                current.next = new_node
                new_node.prev = current
                self.size += 1
                return
            current = current.next
        print("Key not found, nothing added")
        return

    def add_before_key(self, key, val):
        if self._is_empty():
            print("List empty, nothing added")
            return
        current = self.head
        while current:
            if current.data == key:
                break
            current = current.next
        if current == None:
            print("Key not found, nothing added")
            return
        if current.prev == None:
            self.add_node_to_start(val)
            return
        new_node = Node(val)
        previous = current.prev
        previous.next = new_node
        new_node.next = current
        current.prev = new_node
        self.size += 1
        return

    def remove_from_start(self):
        if self._is_empty():
            print("List empty, nothing removed")
            return
        if self.head.next == None:
            self.head = None
            self.size -= 1
            return
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return

    def remove_from_end(self):
        if self._is_empty():
            print("List empty, nothing removed")
            return
        current = self.head
        if current.next == None:
            self.head = None
            self.size -= 1
            return
        while current.next != None:
            current = current.next
        current.prev.next = None
        current = None
        self.size -= 1
        return

    def remove_key(self, key):
        if self._is_empty():
            print("List empty, nothing removed")
            return
        current = self.head
        while current:
            if current.data == key:
                break
            current = current.next
        if current.prev == None:
            self.remove_from_start()
            return
        if current.next == None:
            self.remove_from_end()
            return
        current.prev.next = current.next
        current = None
        self.size -= 1
        return

    def traverse(self, callback):
        if self._is_empty():
            print("List empty")
            return
        current = self.head
        while current:
            callback(current.data)
            current = current.next


d_list = DoublyLinkedList()
d_list.add_node_to_start(10)
d_list.add_node_to_end(100)
d_list.add_after_key("very end", "after very end")
d_list.add_before_key(10, "before 10")
d_list.traverse(print)
print(d_list.get_size())
print("--------------")
d_list.remove_from_start()
d_list.remove_from_end()
d_list.add_node_to_start("start")
d_list.add_after_key("start", "middle")
d_list.add_node_to_end("end")
d_list.traverse(print)
print(d_list.get_size())
print("--------------")
d_list.remove_key("start")
d_list.remove_key("middle")
d_list.remove_key("end")
d_list.traverse(print)
print(d_list.get_size())
