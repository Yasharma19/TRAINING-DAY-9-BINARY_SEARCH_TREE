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
    if ((root.left is not None and find_path(root.left, path, k)) or
            (root.right!=None and find_path(root.right, path, k))):
        return True
    path.pop()
    return False

def print_path(arr, node_a, node_b):
    path_a = []
    path_b = []

    if not find_path(root, path_a, node_a) or not find_path(root, path_b, node_b):
        return "No path found"

    i = 0
    while i < len(path_a) and i < len(path_b):
        if path_a[i] != path_b[i]:
            break
        i += 1

    path = path_a[:i-1:-1] + path_b[i-1:]
    return " ".join(str(node) for node in path)

# Driver code
n = int(input())
tree_array = list(map(int, input().split()))
node_a, node_b = map(int, input().split())
root = construct_bst(tree_array)
print(print_path(root, node_a, node_b))