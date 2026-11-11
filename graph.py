
graph = {
    'T': ['E', 'O'],
    'E': ['C', 'T'],
    'C': ['E', 'I'],
    'I': ['C', 'O'],
    'O': ['I', 'T']
}

def BFS(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def DFS(graph, vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

print("GRAPH TRAVERSAL")

print("\nBFS Traversal:")
BFS(graph, 'T')

print("\nDFS Traversal:")
DFS(graph, 'T')

print()
