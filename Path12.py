class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct_bst(arr):
    root = None
    for num in arr:
        node = TreeNode(num)
        if root is None:
            root = node
        else:
            insert_node(root, node)
    return root

def insert_node(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert_node(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert_node(root.left, node)

def find_path(root, path, k):
    if root is None:
        return False

    path.append(root.val)

    if root.val == k:
        return True

    if ((root.left != None and find_path(root.left, path, k)) or
            (root.right != None and find_path(root.right, path, k))):
        return True

    path.pop()
    return False

def print_path_to_node(root, k):
    path = []
    if find_path(root, path, k):
        print(" ".join(str(x) for x in path))
    else:
        print("No path found")

# Driver code
n = int(input())
tree_array = list(map(int, input().split()))
k = int(input())
root = construct_bst(tree_array)
print_path_to_node(root, k)