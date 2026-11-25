class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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
                if new_node.key<temp.key:
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

    def inorder(self,rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.key, end=" ")
            self.inorder(rt.right)

    def preorder(self,rt):
        if rt is None:
            return
        else:
            print(rt.key, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    def postorder(self,rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.key , end=" ")

        
    def search(self,key):
            temp=self.root
            while temp:
                if temp.key==key:
                    return True
                elif key<temp.key:
                    temp=temp.left
                else:
                    temp=temp.right
            return False


    def find_min_max(self,rt):
        temp=rt
        while temp.left:
            temp=temp.left
        print("Min value:",temp.key)
        temp=rt
        while temp.right:
            temp=temp.right
        print("Max value:",temp.key)

    def del_node(self, rt, val):
            if rt is None:
                return None
            if val < rt.key:
                rt.left = self.del_node(rt.left, val)
            elif val > rt.key:
                rt.right = self.del_node(rt.right, val)
            else:
                if rt.left is None:
                    return rt.right
                if rt.right is None:
                    return rt.left
                succ = self.get_succ(rt)
                rt.key = succ.key
                rt.right = self.del_node(rt.right, succ.key)
            return rt

    def get_succ(self, temp):
        temp = temp.right
        while temp.left is not None:
            temp = temp.left
        return temp

btree = BST()

user_input = input("Enter product IDs separated by spaces: ")
ids = list(map(int, user_input.split()))

for i in ids:
    btree.insert(Node(i))

print("\nProduct IDs in ascending order:")
btree.inorder(btree.root)

search_id = int(input("\n\nEnter product ID to search: "))
print(f"Search {search_id}:", btree.search(search_id))

del_id = int(input("\nEnter product ID to delete: "))
btree.root = btree.del_node(btree.root, del_id)  

print(f"\nAfter deleting {del_id}:")
print("Inorder:  ", end="")
btree.inorder(btree.root)

print("\nPreorder: ", end="")
btree.preorder(btree.root)

print("\nPostorder:", end="")
btree.postorder(btree.root)

print("\n\nThe minimum and maximum product IDs:")
btree.find_min_max(btree.root)