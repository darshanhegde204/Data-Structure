#Stack using Linked List
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None

    def isempty(self):
        return self.top is None
    
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            print("poped Element: ",temp.data)
            self.top=self.top.next
            temp=None
    
    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print ("Stack Values")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next

    def rev_stack(self):
        temp=self.top
        while temp:
            st1.push(Node(temp.data))
            temp=temp.next

    


st=Stack()
st1=Stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.pop()
st.print()
st.rev_stack()
st1.print()
