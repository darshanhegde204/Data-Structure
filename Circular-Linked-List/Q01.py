#Circular Singly Linear Linked List
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
            new_node.next=self.head
        else:
            temp=self.head
            while (temp.next!=self.head):
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head


    def insert(self,new_node,pos):
        if pos==1:
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            new_node.next=self.head
            self.head=new_node
            temp.next=self.head
        else:
            p=1
            temp=self.head
            while (p!=pos-1):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node


    def del_node(self,value):
        temp=self.head
        prev=None
        if temp.data==value:
            while (temp.next!=self.head):
                temp=temp.next
            self.head=self.head.next
            temp.next=self.head
            return
        else:
            while(temp.data!=value):
                prev=temp
                temp=temp.next
                if temp==self.head:
                    print("Value is not there in the list")
                    return
        prev.next=temp.next
        temp=None


    def display(self):
        temp=self.head
        while (True):
            print(temp.data)
            temp=temp.next
            if temp==self.head:
                break

list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.insert(Node(40),4)
# list.insert(Node(5),1)
#list.insert(Node(50),10)
list.del_node(10)
list.display()
