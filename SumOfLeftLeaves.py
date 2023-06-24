class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumLeftLeaves(root):
    if not root:
        return 0

    def isLeaf(node):
        return node and not node.left and not node.right

    def helper(node):
        if not node:
            return 0

        left_sum = 0
        if node.left:
            if isLeaf(node.left):
                left_sum += node.left.val
            else:
                left_sum += helper(node.left)

        right_sum = helper(node.right)

        return left_sum + right_sum

    return helper(root)


# Main function to read input and print output
def main():
    n = int(input())
    nodes = list(map(int, input().split()))

    # Build the binary search tree
    root = None
    if n > 0:
        root = TreeNode(nodes[0])
        for i in range(1, n):
            value = nodes[i]
            node = TreeNode(value)

            curr = root
            while True:
                if value < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        break

    # Calculate and print the sum of left leaves
    left_sum = sumLeftLeaves(root)
    print(left_sum)


# Run the main function
if __name__ == "__main__":
    main()