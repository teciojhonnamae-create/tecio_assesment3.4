
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node("T")
root.left = Node("E")
root.right = Node("O")
root.left.left = Node("C")
root.left.right = Node("I")

def BFS(root):
    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

def DFS(root):
    if root is None:
        return

    print(root.value, end=" ")
    DFS(root.left)
    DFS(root.right)

print("BINARY TREE TRAVERSAL")
print("\nBFS Traversal:")
BFS(root)

print("\nDFS Traversal:")
DFS(root)

print()
