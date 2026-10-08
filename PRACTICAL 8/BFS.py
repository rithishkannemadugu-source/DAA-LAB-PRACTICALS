def bfs(adj):
    V = len(adj)
    visited = [False] * V
    res = []
    src = 0
    queue = []

    visited[src] = True
    res.append(src)
    queue.append(src)

    while queue:
        curr = queue.pop(0)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                res.append(i)
                queue.append(i)

    return res


graph = {
    0: [1, 5],
    1: [0, 2, 4, 3],
    2: [1, 4],
    3: [1, 4, 6],
    4: [1, 2, 3, 5],
    5: [0, 4],
    6: [3]
}

result = bfs(graph)
print(result)
