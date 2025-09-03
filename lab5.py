from collections import deque

class Graph:
    def _init_(self):
        self.list1 = {}

    def _str_(self):
        return str(self.list1)

    def addedge(self, p, c):
        if p not in self.list1:
            self.list1[p] = []
        self.list1[p].append(c)

    def BFS(self, s, g):
        visited = {key: False for key in self.list1}  # Dictionary for visited nodes
        queue = deque([s])  # Use deque for efficient popping from the left
        
        visited[s] = True

        while queue:
            current = queue.popleft()  # Get the first element from the queue
            print(current, end=" ")

            if current == g:
                print("\nGOAL NODE FOUND...!!!")
                return 1
            
            # Iterate over the neighbors of the current vertex
            for neighbor in self.list1.get(current, []):  # Get neighbors; default to empty list
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        # If the goal node is not found
        print("\nGOAL NODE NOT FOUND!")
        return 0

g = Graph()
g.addedge('A', 'B')
g.addedge('A', 'C')
g.addedge('B', 'D')
g.addedge('B', 'E')
g.addedge('B', 'K')
g.addedge('B', 'J')
g.addedge('B', 'A')
g.addedge('F', 'A')
g.addedge('D', 'G')
g.addedge('D', 'A')
g.addedge('E', 'C')
g.addedge('E', 'H')
g.addedge('E', 'I')
g.addedge('E', 'A')
g.addedge('K', 'N')
g.addedge('K', 'M')
g.addedge('K', 'B')
g.addedge('J', 'B')
g.addedge('G', 'D')
g.addedge('C', 'I')
g.addedge('H', 'I')
g.addedge('I', 'I')
g.addedge('I', 'E')
g.addedge('I', 'L')
g.addedge('N', 'K')
g.addedge('M', 'K')
g.addedge('L', 'I')

print(g)
print("The BFS Traversal of the Graph is:")
g.BFS('A', 'G')
# priority queue
class PriorityQueue:
    def _init_(self):
        self.list = []

    def enqueue(self, item, priority):
        # Add the item as a tuple (priority, item)
        self.list.append((priority, item))
        # Sort the list based on priority without using lambda
        self.list.sort(key=self.get_priority)

    def get_priority(self, item):
        # Extract the priority from the tuple
        return item[0]

    def dequeue(self):
        # Remove and return the item with the highest priority (lowest number)
        if self.list:
            return self.list.pop(0)[1]  # Return only the item, not the priority
        else:
            raise IndexError("Dequeue from an empty priority queue")
        

# Create an instance of PriorityQueue
pq = PriorityQueue()
# Enqueue items with their priorities
pq.enqueue(10, 2)  # Item 10 with priority 2
pq.enqueue(20, 1)  # Item 20 with priority 1
pq.enqueue(30, 3)  # Item 30 with priority 3

# Dequeue to get the item with the highest priority
print(pq.dequeue())  # Should print 20 (highest priority)