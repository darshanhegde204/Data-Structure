#Double ended Queue using linked list
class node:
    def __init__(self, value):
        self.data=value
        self.next=None
        
class double_ended_queue:
    def __init__(self):
        self.front=self.rear=None
        
    def enqueue(self, new_node, ch):
        if self.rear==None:
            self.front=self.rear=new_node
            return
        else:
            if ch=='r':
                self.rear.next=new_node
                self.rear=new_node
            else:
                new_node.next=self.front
                self.front=new_node
            
    def dequeue(self, ch):
        if self.rear:
            temp=self.front
            if self.front==self.rear:#deleting last node in queue
                print("Node removed: ", self.front.data)
                self.front=self.rear=None
                print("Queue is empty")
                del temp
                return
            if ch=='f':
                print("Node removed: ", self.front.data)
                self.front=self.front.next
            else:
                while temp.next!=self.rear:
                    temp=temp.next
                temp.next=self.rear.next
                self.rear=temp
            del temp
        else:
            print("Queue is empty")
            
    def print(self):
        temp=self.front
        print("Queue contains...")
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()
            
que=double_ended_queue()
que.enqueue(node(10),'r')
que.enqueue(node(20),'f')        
que.enqueue(node(30),'r')   
que.enqueue(node(40),'f')
que.print()
que.dequeue('f')
que.print()
que.dequeue('r')
que.print()
que.dequeue('f')
que.print()
que.dequeue('f')