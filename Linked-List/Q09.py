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

    def concatenate(self, head):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = head



list1 = LinkedList()
list1.append(Node(10))
list1.append(Node(20))

print("List 1:")
list1.display()

list2 = LinkedList()
list2.append(Node(30))
list2.append(Node(40))

print("\nList 2:")
list2.display()

print("\nAfter Concatenating:")
list1.concatenate(list2.head)
list1.display()