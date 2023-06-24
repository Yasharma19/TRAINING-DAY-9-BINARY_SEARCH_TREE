from collections import deque
def check_binary_search_tree_(root, lowest_value=0, highest_value=10000):
    min_v = lowest_value - 1
    max_v = highest_value + 1
    q = deque([(root, min_v, max_v)])
    while q:
        node, min_val, max_val = q.popleft()
        if not node: continue
        if node.data >= max_val or node.data <= min_val: return False
        if node.left: q.append((node.left, min_val, node.data))
        if node.right: q.append((node.right, node.data, max_val))
    return True