# Singly Linear Linked List
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete_alternate(self):
        prev = self.head
        temp = self.head.next
        while prev and temp:
            prev.next = temp.next
            prev = prev.next
            if prev:
                temp = prev.next
            else:
                temp = None


my_list = LinkedList()
my_list.append(Node(10))
my_list.append(Node(20))
my_list.append(Node(30))
my_list.append(Node(40))
my_list.append(Node(50))

print("Original List:")
my_list.display()

print("\nAfter deleting alternate nodes:")
my_list.delete_alternate()
my_list.display()