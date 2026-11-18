#Linear Queue
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        
    
    def dequeue(self):
        if self.rear==None:
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create a queue
myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")
myQueue.printQueue()
print("Dequeue: ", myQueue.dequeue())
print("Dequeue: ", myQueue.dequeue())
print("Dequeue: ", myQueue.dequeue())
print("Dequeue: ", myQueue.dequeue())