class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



root = Node("J")

root.left = Node("H")
root.right = Node("T")

root.left.left = Node("O")
root.left.right = Node("N1")

root.left.left.left = Node("N2")
root.left.left.right = Node("A")

root.right.left = Node("E")
root.right.right = Node("C")

root.right.left.left = Node("I")
root.right.left.right = Node("O")



def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)



def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")



print("Preorder Traversal:")
preorder(root)

print("\n\nInorder Traversal:")
inorder(root)

print("\n\nPostorder Traversal:")
postorder(root)

print()