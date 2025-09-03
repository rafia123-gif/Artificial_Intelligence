#Greedy first search -->general code 
#task 1:
import heapq
# Graph connections
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (just estimates to goal 'F')
heuristic = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}


def greedy_best_first_search(graph, start, goal, heuristic):
    # priority queue (min-heap) based on heuristic
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start, [start]))
    visited = set()

    while open_list:
        h, node, path = heapq.heappop(open_list)

        if node == goal:
            return path   # return the solution path

        if node in visited:
            continue
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None

path = greedy_best_first_search(graph, 'A', 'F', heuristic)
print("Path found:", path)
#A* code 
#task 2:
graph = {
    'A': [('B', 1), ('C', 4), ('D', 3)],
    'B': [('E', 6)],
    'C': [('F', 2)],
    'D': [('G', 5)],
    'E': [],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values (straight-line estimate to G)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 5,
    'F': 1,
    'G': 0
}
import heapq

def a_star_search(graph, start, goal, heuristic):
    # priority queue (min-heap)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    visited = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            return path

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                g_new = g + cost
                h_new = heuristic[neighbor]
                f_new = g_new + h_new
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None

path = a_star_search(graph, 'A', 'G', heuristic)
print("Path found:", path)
#task 3
import heapq

# Heuristic: Manhattan Distance
def manhattan_distance(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:  # ignore blank
            goal_index = goal.index(state[i])
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(goal_index, 3)
            distance += abs(r1 - r2) + abs(c1 - c2)
    return distance

# Generate neighbors by sliding blank
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)  # blank position
    row, col = divmod(idx, 3)

    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors

# A* Search Algorithm
def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start, goal), 0, start, []))
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                g_new = g + 1
                h_new = manhattan_distance(neighbor, goal)
                f_new = g_new + h_new
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [state]))

    return None

# Pretty print
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print("------")

# Example Run
if __name__ == "__main__":
    start = (1,2,3,
             4,5,6,
             7,8,0)   # you can change start state here

    goal = (0,1,2,
            3,4,5,
            6,7,8)

    print("Solving 8 Puzzle using A* Search...\n")
    path = a_star(start, goal)

    if path:
        for step in path:
            print_board(step)
        print(f"✅ Solved in {len(path)-1} moves")
    else:
        print("❌ No solution found.")


