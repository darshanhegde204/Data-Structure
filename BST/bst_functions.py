class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.count=0
        self.lcount=0
        self.nlcount=0

    def insert(self, new_node):
        if self.root is None:
            self.root=new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    
    def inorder(self,temp):
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data, end=" ")
            self.count+=1
            if temp.left is None and temp.right is None:
                self.lcount+=1
            if temp.left is not None or temp.right is not None:
                self.nlcount+=1
            self.inorder(temp.right)

    def find_minmax(self,rt):
        temp=rt
        while temp.left:
            temp=temp.left
        print("\n Min value:",temp.data)
        temp=rt
        while temp.right:
            temp=temp.right
        print("\n Max value:",temp.data)

btree=BST()
btree.insert(Node(100))
btree.insert(Node(10))
btree.insert(Node(450))
btree.insert(Node(4))
btree.insert(Node(65))
btree.insert(Node(50))
btree.insert(Node(300))
btree.insert(Node(500))
btree.inorder(btree.root)
print("\n Total nodes :", btree.count)
print("\n Total leaf Node: ", btree.lcount)
print("\n total non-leaf Node:",btree.nlcount)
btree.find_minmax(btree.root)