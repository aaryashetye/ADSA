class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(node, target):
    if node is None:
        return None 
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

root = TreeNode(25)
node20 = TreeNode(20)
node30 = TreeNode(30)
node15 = TreeNode(15)
node21 = TreeNode(21)
node26 = TreeNode(26)
node31 = TreeNode(31)

root.left = node20
root.right = node30

node20.left = node15
node20.right = node21

node30.left = node26
node30.right = node31


result = search(root.right, 30)
if result:
    print(f"Found the node with value: {result.data}")
else:
    print("Value not found in the BST.")


result = search(root, 40)
if result:
    print(f"Found the node with value: {result.data}")
else:
    print("Value not found in the BST.")