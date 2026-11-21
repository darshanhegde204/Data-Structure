#circular Queue using linked list
class node:
    def __init__(self, value):
        self.data=value
        self.next=None
        
class circular_queue:
    def __init__(self):
        self.front=self.rear=None
        
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node #update rear pointer
        else:
            self.front=self.rear=new_node
        new_node.next=self.front
        return
        
    def print(self):
        temp=self.front
        while True:
            print(temp.data, end=" ")
            temp=temp.next
            if temp==self.front:
                break
        print()
        
    def dequeue(self):
        if self.rear!=None:
            temp=self.front
            print("Node deleted...", temp.data)
            if self.front==self.rear: #deleting last node in queue
                self.front=self.rear=None
            else:
                self.front=self.front.next
                self.rear.next=self.front
            del temp
            return
        else:
            print("Queue is empty...")
            
    
que=circular_queue()
que.enqueue(node(10))
que.enqueue(node(20))
que.enqueue(node(30))   
que.enqueue(node(40))
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()
que.dequeue()
que.dequeue()



