# 1. Create Linked List-append (create nodes with positive and negative
# numbers)
# 2. Traverse and print the node values
# 3. Insert node at a specific position
# 4. Delete the nodes having negative values

class Node:
    def __init__(self,data):
        self.next=None
        self.data=data

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while (temp.next):
                temp=temp.next
            temp.next=newnode

    def display(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next

    def insert(self,newnode,pos):
        if pos==1:
            newnode.next=self.head
            self.head=newnode
        else:
            p=1
            temp=self.head
            while (p!=pos-1 and temp.next):
                temp=temp.next
                p+=1
            newnode.next=temp.next
            temp.next=newnode

    def delval(self):
        temp=self.head
        prev=None
        while (temp!=None):
            if temp.data<0:
                if temp==self.head:
                    self.head=temp.next
                    temp=self.head
                else:
                    prev.next=temp.next
                    temp=prev.next
            else:
                prev=temp
                temp=temp.next


ll=LinkedList()

print("Traverse and printing the node values")
n = int
ll.append(Node(5))
ll.append(Node(10))
ll.append(Node(-3))
ll.append(Node(25))
ll.append(Node(-15))
ll.append(Node(18))
ll.display()

print("Linked List-after Insert")
ll.insert(Node(-1),1)
ll.insert(Node(-4),4)
ll.insert(Node(11),9)
ll.display()

print("Before Deleting Negative values")
ll.display()

ll.delval()

print("After Deleting Negative values")
ll.display()



