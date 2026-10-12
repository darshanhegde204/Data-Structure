
#Singly Linear Linked List
class Node:
    def __init__(self, val ):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self, new_node):
        if (self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while (temp.next):
                temp=temp.next
            temp.next=new_node

    def display(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next
    def delete_first_and_last(self):
        self.head = self.head.next
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.display()
list.delete_first_and_last()
list.display()



