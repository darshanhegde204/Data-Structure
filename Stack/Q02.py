# Stack using Linked List
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None
    
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            print("popped Element: ", temp.data)
            self.top = self.top.next
            temp = None
    
    def peek(self):
        """Returns the value at the top of the stack without removing it."""
        if self.isempty():
            print("Stack is empty")
            return None
        else:
            return self.top.data

    def search(self, value):
        """Searches for a value in the stack and prints its position from the top."""
        if self.isempty():
            print("Stack is empty")
            return False
        
        temp = self.top
        position = 1
        while temp:
            if temp.data == value:
                print(f"Value {value} found at position {position} from the top.")
                return True
            temp = temp.next
            position += 1
            
        print(f"Value {value} not found in the stack.")
        return False

    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack Values:")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

    def rev_stack(self):
        temp = self.top
        while temp:
            st1.push(Node(temp.data))
            temp = temp.next


# Driver Code
st = Stack()
st1 = Stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))

# Test Peek
print("Top element (Peek):", st.peek())

# Test Search
st.search(30)
st.search(100)

st.pop()
st.print()

st.rev_stack()
st1.print()