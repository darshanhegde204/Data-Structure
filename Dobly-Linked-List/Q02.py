class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
            
        temp = self.head
        p = 1
        while p < pos - 1 and temp.next:
            temp = temp.next
            p += 1
        new_node.next = temp.next
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

    def reverse(self):
        current = self.head
        last_node = None
        # The while loop naturally skips execution if current is None
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            last_node = current
            current = current.prev
            
        self.head = last_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# --- Test ---
ll = LinkedList()
ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.insert(Node(5), 2)

print("Original List:")
ll.display()

ll.reverse()

print("\nReversed List:")
ll.display()