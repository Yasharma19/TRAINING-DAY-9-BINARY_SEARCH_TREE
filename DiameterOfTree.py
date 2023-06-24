class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def str(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
def height(node):
    if not node:
        return 0
    return max(height(node.left),height(node.right))+1

def diameter(root):
    if not root:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    ldia=diameter(root.left)
    rdia=diameter(root.right)
    return max(lheight+rheight+1,max(ldia,rdia))
tree=BinarySearchTree()
n=int(input())
l=list(map(int,input().split()))
for i in l:
    tree.create(i)
print(diameter(tree.root))