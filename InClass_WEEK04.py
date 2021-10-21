
def bfs(graph, root):
    visited = []
    queue = []
    queue.append(root)

    while queue:
        print(queue)
        vertex = queue.pop(0)
        print(vertex)

        visited.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
if __name__ =='__main__':
    graph = {
        "A":['B','C'],
        "B":['D','E'],
        "C":['F','G'],
        "D":['H','I'],
        "H":[],
        "I":[],
        "E":['J','K'],
        "J":[],
        "K":[],
        "F":['L','M'],
        "L":[],
        "M":[],
        "G":['N','O'],
        "N":[],
        "O":[]
    }
    print(graph)
    print("Following is Breadth First Traversal: ")
    bfs(graph,'A')

def dfs(visited, graph ,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited,graph,neighbor)
if __name__ =='__main__':
    graph = {
        "A":['B','C'],
        "B":['D','E'],
        "C":['F','G'],
        "D":['H','I'],
        "H":[],
        "I":[],
        "E":['J','K'],
        "J":[],
        "K":[],
        "F":['L','M'],
        "L":[],
        "M":[],
        "G":['N','O'],
        "N":[],
        "O":[]
    }
    print(graph)
    print("Following is Depth First Traversal: ")
    visited = set()
    dfs(visited, graph, 'A')