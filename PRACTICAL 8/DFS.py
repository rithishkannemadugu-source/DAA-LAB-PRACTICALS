def dfs(adj):
    V = len(adj)

    # Keep track of visited vertices
    visited = [False] * V

    # Store DFS traversal
    res = []

    # Starting vertex
    src = 0

    # Stack for DFS
    stack = []

    # Mark source as visited
    visited[src] = True
    res.append(src)

    # Push source and its neighbor iterator
    stack.append((src, iter(adj[src])))

    # Continue until stack becomes empty
    while stack:

        curr, neighbors = stack[-1]

        # Find the next unvisited neighbor
        for i in neighbors:
            if not visited[i]:
                # Mark neighbor as visited
                visited[i] = True

                # Add to DFS result
                res.append(i)

                # Push only this neighbor
                stack.append((i, iter(adj[i])))

                # Go deeper before checking other neighbors
                break

        else:
            # No unvisited neighbors: backtrack
            stack.pop()
            print(stack)

    return res


# Graph
graph = {
    0: [1, 5],
    1: [0, 2, 4, 3],
    2: [1, 4],
    3: [1, 4, 6],
    4: [1, 2, 3, 5],
    5: [0, 4],
    6: [3]
}

# Perform DFS
result = dfs(graph)
print(result)