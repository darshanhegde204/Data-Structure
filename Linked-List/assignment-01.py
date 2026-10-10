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
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while p != pos - 1 and temp.next:
                temp = temp.next
                p += 1
            if temp:
                new_node.next = temp.next
                temp.next = new_node

    def find_middle(self):
        if not self.head:
            print("The list is empty.")
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"Middle node value: {slow.data}")

    def del_node(self,value):
            temp=self.head
            prev=None
            if temp.data==value:
                self.head=self.head.next
                return
            while(temp):
                if temp.data==value:
                    break
                else:
                    prev=temp
                    temp=temp.next
            if temp==None:
                print("Value is not there in the list")
                return
            prev.next=temp.next
            temp=None

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        self.head = prev

    def sum_consecutive(self):
        if not self.head or not self.head.next:
            print("Not enough nodes to calculate consecutive sums.")
            return
        temp = self.head
        print("Sum of every two consecutive node pairs:")
        while temp and temp.next:
            pair_sum = temp.data + temp.next.data
            print(f"({temp.data} + {temp.next.data}) = {pair_sum}")
            temp = temp.next.next  # Move forward by 2 nodes for non-overlapping pairs



my_list = LinkedList()
    
    
my_list.append(Node(10))
my_list.append(Node(20))
my_list.append(Node(30))
my_list.append(Node(40))
my_list.append(Node(50))

print("Initial List:")
my_list.display()
    
my_list.insert(Node(25), 3)
print("After inserting 25 at position 3:")
my_list.display()

my_list.find_middle()

my_list.del_node(20)
print("After deleting 20:")
my_list.display()

my_list.sum_consecutive()

my_list.reverse()
print("After reversing the list:")
my_list.display()