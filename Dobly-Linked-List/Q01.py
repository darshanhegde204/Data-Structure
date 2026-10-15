class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
        else:
            self.head=new_node

    def insert(self,new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        else:
            p=1
            while(p!=pos-1 and temp.next):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            new_node.next=temp.next
            if temp.next:
                temp.next.prev=new_node
            temp.next=new_node
            new_node.prev=temp

    def display(self):
            temp=self.head
            while (temp):
                print(temp.data)
                temp=temp.next

ll = LinkedList()
ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.insert(Node(5),2)
    
ll.display()
