class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None

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
            self.inorder(temp.right)
    
    def del_node(self, rt, val):
        if rt is None:
            return None
        if val < rt.data:
            rt.left = self.del_node(rt.left, val)
        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)
        else:
            if rt.left is None:
                return rt.right
            if rt.right is None:
                return rt.left
            succ = self.get_succ(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)
        return rt

    def get_succ(self, temp):
        temp = temp.right
        while temp.left is not None:
            temp = temp.left
        return temp

    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False
        

btree=BST()
btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(15))
btree.insert(Node(2))
btree.insert(Node(8))
btree.insert(Node(20))
btree.insert(Node(13))
btree.inorder(btree.root)
btree.del_node(btree.root,2)
print("\n after delete ")
btree.inorder(btree.root)
if btree.search(15):
    print("\n found the note")
else:
    print("\n Not Found")
