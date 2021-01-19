# Singly Linked List Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next_node = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self, callback):
        current = self.head
        while current is not None:
            callback(current.data)
            current = current.next_node

    def get_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def add_to_start(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        new_node.next_node = self.head
        self.head = new_node
        return

    def add_to_end(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node
        return

    def add_after_key(self, key, val):
        if self.head == None:
            print("linked list empty")
            return
        new_node = Node(val)
        current = self.head
        while current.next_node:
            if current.data == key:
                new_node.next_node = current.next_node
                current.next_node = new_node
                return
            current = current.next_node
        print("key not found")
        return

    def add_before_key(self, key, val):
        if self.head == None:
            print("linked list empty")
            return
        if self.head.data == key:
            self.add_to_start(val)
            return
        new_node = Node(val)
        current = self.head
        while current.next_node:
            if current.next_node.data == key:
                new_node.next_node = current.next_node
                current.next_node = new_node
                return
            current = current.next_node
        print("key not found")
        return

    def find_key(self, key):
        current = self.head
        found = False
        if current == None:
            print("list empty")
            return found
        while current:
            if current.data == key:
                found = True
                return found
            current = current.next_node
        return found

    #    def delete_key(self, key):
    #        if self.head == None:
    #            print("linked list empty")
    #            return
    #        current = self.head
    #        if current.data == key:
    #            new_node = self.head.next_node
    #            self.head = new_node
    #            return
    #        current = self.head
    #        while current and current.next_node:
    #            if current.next_node.data == key:
    #                if current.next_node.next_node is not None:
    #                    new_node = current.next_node.next_node
    #                    current.next_node = new_node
    #                    return
    #                else:
    #                    current.next_node = None
    #            current = current.next_node
    #        print("key not found")
    #        return

    def delete_key(self, key):
        current = self.head
        previous = None
        found = False
        while current and found == False:
            if current.data == key:
                found = True
            else:
                previous = current
                current = current.next_node
        if current == None:
            print("Key not in list")
            return
        if previous == None:
            self.head = current.next_node
        else:
            previous.next_node = current.next_node


day_list = SinglyLinkedList()
day_list.head = Node("Mon")
e2 = Node("Tue")
day_list.head.next_node = e2
# day_list.traverse_list(print)
# print("-------------------")
day_list.add_to_start("Sun")
# day_list.traverse_list(print)
# print("-------------------")
day_list.add_to_end("Wed")
# day_list.traverse_list(print)
# print("-------------------")
day_list.add_after_key("Tue", "Second Tue")
# day_list.traverse_list(print)
# print("-------------------")
day_list.add_before_key("Tue", "Second Mon")
# day_list.traverse_list(print)
# print("-------------------")
day_list.add_after_key("Thu", "Second Thu")
# day_list.traverse_list(print)
# print("-------------------")
day_list.add_before_key("Thu", "Second Mon")
# day_list.traverse_list(print)
# print("-------------------")
# day_list.delete_key('Second Tue')
# day_list.traverse_list(print)
# print("-------------------")
# day_list.delete_key('Tue')
# day_list.traverse_list(print)
# print("-------------------")
# day_list.delete_key('Sun')
# day_list.traverse_list(print)
print("-------------------")
day_list.delete_key("Wed")
day_list.traverse_list(print)
print("--------Get Size--------")
print(day_list.get_size())
print("--------Find Key--------")
print(day_list.find_key("Second Tue"))

print(day_list.find_key("Mon"))
print(day_list.find_key("Hello"))
print("------Before Delete------")
day_list.traverse_list(print)
day_list.delete_key("Second Tue")
day_list.delete_key("Thu")
print("------After Delete------")
day_list.traverse_list(print)
