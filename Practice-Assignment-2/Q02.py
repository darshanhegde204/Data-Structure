# Question 2

class node:
    def __init__(self, value):
        self.data = value
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = self.front.next
            if self.front == None:
                self.rear = None
                
            temp.next = None 
            
            return temp
        else:
            print("Queue is empty")
            return None

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
    # 4. Reverse the queue using stack
    def reverse(self):
        stack = []

        while self.front:
            stack.append(self.dequeue())

        while stack:
            self.enqueue(stack.pop())

    # 5. Merge two queues into one
    def merge(self, q2):
        if not self.front:
            self.front = q2.front
            self.rear = q2.rear
        elif q2.front:
            self.rear.next = q2.front
            self.rear = q2.rear

        q2.front = q2.rear = None

    # 6. Check if two queues are identical
    def is_identical(self, q2):
        temp1 = self.front
        temp2 = q2.front
        
        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
            
        return temp1 == None and temp2 == None


q1 = queue()
q1.enqueue(node(10))
q1.enqueue(node(20))
q1.enqueue(node(30))

print("Original Queue 1:")
q1.print()

print("\nAfter 1 Dequeue:")
q1.dequeue()
q1.print()

print("\nReversed Queue:")
q1.reverse()
q1.print()

print("\n--- Merge & Identical Check ---")
q2 = queue()
q2.enqueue(node(30))
q2.enqueue(node(20))

print("Is q1 identical to q2?", q1.is_identical(q2))

q3 = queue()
q3.enqueue(node(40))
q3.enqueue(node(50))

q1.merge(q3)
print("Queue 1 after merging with Queue 3:")
q1.print()