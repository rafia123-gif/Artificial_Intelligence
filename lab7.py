# Tree representation
graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'K': ['N', 'M'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'C': [], 'H': [], 'I': ['L'],
    'J': [], 'N': [], 'M': [],
    'L': [],
    'G': []  # Goal
}

# Depth Limited Search
def depth_limited_search(node, goal, depth_limit):
    if node == goal:
        return [node]
    if depth_limit <= 0:
        return None
    for child in graph[node]:
        path = depth_limited_search(child, goal, depth_limit - 1) # recursive call
        if path: # If goal found in this child's subtree
            return [node] + path # Add current node to the path
    return None

# Iterative Deepening Search
def iterative_deepening_search(start, goal):
    depth = 0
    while True:
        path = depth_limited_search(start, goal, depth)
        if path:
            return path, depth
        depth += 1

# Example runs
print("Depth Limited Search (limit=3):", depth_limited_search('A', 'L', 1))
print("Iterative Deepening Search:", iterative_deepening_search('A', 'M'))

# Comparison:

# | **Criteria**               | **Depth Limited Search**                | **Iterative Deepening Search**          |
# | -------------------------- | --------------------------------------- | --------------------------------------- |
# | Completeness               | No (fails if goal is deeper than limit) | Yes (guaranteed to find goal if exists) |
# | Optimality (shortest path) | No (depends on limit chosen)            | Yes (always finds shallowest goal)      |
# | Time complexity            | O(b^l)                                  | O(b^d) (same as BFS in worst case)      |
# | Space complexity           | O(b * l)                                | O(b * d) (linear in depth)             |
# 👉 Best for this tree: Iterative Deepening Search (IDS), because it guarantees finding the goal even if we don’t know the depth in advance.