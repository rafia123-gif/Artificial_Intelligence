# # task 1:(may be some mistake)
# class Tree:
#     def __init__(self, size):
#         self.tree = [[] for _ in range(size)]

#     def add_edge(self, parent, child):
#         self.tree[parent].append(child)

#     def DFS(self, root):
#         stack = [root]
#         visited = set()

#         while stack:
#             node = stack.pop()
#             if node not in visited:
#                 print(node, end=" ")
#                 visited.add(node)
#                 # Add children to the stack in reverse order for correct DFS order
#                 stack.extend(reversed(self.tree[node]))

# # Create the tree
# tree = Tree(12)
# tree.add_edge(1,2)
# tree.add_edge(1,7)
# tree.add_edge(1,8)
# tree.add_edge(2,3)
# tree.add_edge(2,6)
# tree.add_edge(3,4)
# tree.add_edge(3,5)
# tree.add_edge(8,9)
# tree.add_edge(8,12)
# tree.add_edge(9,10)
# tree.add_edge(9,11)
# print("\nDFS traversal of the tree starting from node 1:")
# tree.DFS(1)
# Task 1: Simplified Tree Implementation
class Tree:
    def __init__(self):
        self.tree = {}

    def add_edge(self, parent, child):
        # Use setdefault to add the child efficiently
        # This line does three things in one:
        # 1-self.tree is a dictionary that stores the adjacency list of the tree.
        # Example: self.tree = {1: [2, 3], 2: [4], ...}
        # 2-setdefault(parent, []):
        # If parent already exists in the dictionary, it returns the existing list of children.
        # If parent is not yet in the dictionary, it:
        # Adds parent to self.tree with an empty list [] as its value
        # Then returns that empty list.
        # 3-.append(child):
        # Adds child to the list of children for the parent
        self.tree.setdefault(parent, []).append(child) 

    def DFS(self, root):
        if root not in self.tree and root != 0:
            print(f"Node {root} is not in the tree.")
            return
        
        stack = [root]
        visited = set()

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                # Add children in reverse for correct DFS order
                stack.extend(reversed(self.tree.get(node, [])))

# Create the tree
tree = Tree()
tree.add_edge(1, 2)
tree.add_edge(1, 7)
tree.add_edge(1, 8)
tree.add_edge(2, 3)
tree.add_edge(2, 6)
tree.add_edge(3, 4)
tree.add_edge(3, 5)
tree.add_edge(8, 9)
tree.add_edge(8, 12)
tree.add_edge(9, 10)
tree.add_edge(9, 11)

print("\nDFS traversal of the tree starting from node 1:")
tree.DFS(1)

# task 2
class Tree:
    def __init__(self):
        self.tree = {}

    def add_edge(self, parent, child):
        # Add parent and child to the tree if they don't exist
        if parent not in self.tree:
            self.tree[parent] = []
        if child not in self.tree:
            self.tree[child] = []
        self.tree[parent].append(child)

    def DFS(self, root, goal):
        stack = [root]
        visited = set()

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                
                # Check if the current node is the goal node
                if node == goal:
                    print("\nGoal node found!")
                    return

                # Add children to the stack in reverse order for correct DFS order
                stack.extend(reversed(self.tree[node]))

        print("\nGoal node not found.")

# Create the tree
tree = Tree()
tree.add_edge('A', 'B')
tree.add_edge('A', 'F')
tree.add_edge('A', 'D')
tree.add_edge('A', 'E')
tree.add_edge('B', 'K')
tree.add_edge('B', 'J')
tree.add_edge('K', 'N')
tree.add_edge('K', 'M')
tree.add_edge('D', 'G')
tree.add_edge('E', 'C')
tree.add_edge('E', 'H')
tree.add_edge('E', 'I')
tree.add_edge('I', 'L')

# Perform DFS with character nodes
start_node = 'A'
goal_node = 'G'
print(f"\nDFS traversal of the tree starting from node {start_node} to find {goal_node}:")
tree.DFS(start_node, goal_node)
