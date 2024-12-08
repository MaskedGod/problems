### What are **Graph Algorithms**?
Graph algorithms are used to solve problems related to graphs, which consist of nodes (vertices) connected by edges. These algorithms can help in finding the shortest paths, minimum spanning trees, and ordering nodes in directed graphs.

---

### 1. **Kruskal’s Algorithm**
   - **How it works**:
     - Kruskal’s algorithm finds the minimum spanning tree (MST) of a connected, weighted graph. An MST connects all vertices with the minimum possible total edge weight.
     - The algorithm sorts all edges in non-decreasing order of their weights. It then adds edges to the MST one by one, ensuring that no cycles are formed (using the union-find data structure to check for cycles).

   - **Example Explanation**:
     - Given a graph with weighted edges, the algorithm iteratively adds the lowest-weight edge to the MST until all vertices are connected without cycles.

   **Python Code**:
   ```python
   class UnionFind:
       def __init__(self, size):
           self.parent = list(range(size))
           self.rank = [1] * size

       def find(self, u):
           if self.parent[u] != u:
               self.parent[u] = self.find(self.parent[u])  # Path compression
           return self.parent[u]

       def union(self, u, v):
           root_u = self.find(u)
           root_v = self.find(v)
           if root_u != root_v:
               # Union by rank
               if self.rank[root_u] > self.rank[root_v]:
                   self.parent[root_v] = root_u
               elif self.rank[root_u] < self.rank[root_v]:
                   self.parent[root_u] = root_v
               else:
                   self.parent[root_v] = root_u
                   self.rank[root_u] += 1

   def kruskal(vertices, edges):
       uf = UnionFind(vertices)
       mst = []
       edges.sort(key=lambda x: x[2])  # Sort edges by weight

       for u, v, weight in edges:
           if uf.find(u) != uf.find(v):
               uf.union(u, v)
               mst.append((u, v, weight))

       return mst

   # Example graph: (u, v, weight)
   edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5),
            (1, 3, 15), (2, 3, 4)]
   vertices = 4
   mst = kruskal(vertices, edges)
   print("Minimum Spanning Tree:", mst)
   ```

---

### 2. **Bellman-Ford Algorithm**
   - **How it works**:
     - The Bellman-Ford algorithm finds the shortest paths from a single source vertex to all other vertices in a graph, even if the graph contains negative weight edges.
     - It relaxes all edges repeatedly for a total of \( V-1 \) times (where \( V \) is the number of vertices). After that, it checks for negative weight cycles.

   - **Example Explanation**:
     - Starting from a source vertex, the algorithm updates the shortest path to each vertex until no further updates are possible or until \( V-1 \) iterations are complete.

   **Python Code**:
   ```python
   def bellman_ford(vertices, edges, source):
       # Initialize distances from the source
       distance = [float('inf')] * vertices
       distance[source] = 0

       # Relax edges up to V-1 times
       for _ in range(vertices - 1):
           for u, v, weight in edges:
               if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                   distance[v] = distance[u] + weight

       # Check for negative weight cycles
       for u, v, weight in edges:
           if distance[u] != float('inf') and distance[u] + weight < distance[v]:
               print("Graph contains a negative weight cycle")
               return None

       return distance

   # Example graph: (u, v, weight)
   edges = [(0, 1, -1), (0, 2, 4),
            (1, 2, 3), (1, 3, 2), (1, 4, 2),
            (3, 1, 1), (3, 4, -3),
            (4, 0, 1)]
   vertices = 5
   source = 0
   distances = bellman_ford(vertices, edges, source)
   print("Shortest distances from source:", distances)
   ```

---

### 3. **Topological Sorting**
   - **How it works**:
     - Topological sorting is applicable only to directed acyclic graphs (DAGs). It provides a linear ordering of vertices such that for every directed edge \( u \to v \), vertex \( u \) comes before \( v \) in the ordering.
     - The algorithm can be implemented using either Depth-First Search (DFS) or Kahn’s algorithm (in-degree method).

   - **Example Explanation**:
     - Given a directed acyclic graph, the algorithm processes each vertex, marking it as visited, and pushes it onto a stack. When all vertices are processed, the stack is popped to get the topological order.

   **Python Code (Using DFS)**:
   ```python
   def topological_sort_util(vertex, visited, stack, graph):
       visited[vertex] = True
       for neighbor in graph[vertex]:
           if not visited[neighbor]:
               topological_sort_util(neighbor, visited, stack, graph)
       stack.append(vertex)  # Push to stack after visiting all neighbors

   def topological_sort(vertices, graph):
       visited = [False] * vertices
       stack = []

       for i in range(vertices):
           if not visited[i]:
               topological_sort_util(i, visited, stack, graph)

       return stack[::-1]  # Return reversed stack for topological order

   # Example graph (adjacency list)
   graph = {
       0: [1, 2],
       1: [3],
       2: [3],
       3: [4],
       4: []
   }
   vertices = 5
   order = topological_sort(vertices, graph)
   print("Topological Sort:", order)
   ```

---

### Summary of **Graph Algorithms**:
1. **Kruskal’s Algorithm**: Finds the minimum spanning tree of a graph by adding the lowest-weight edges while avoiding cycles.
2. **Bellman-Ford Algorithm**: Calculates the shortest paths from a single source vertex to all others, handling negative weight edges.
3. **Topological Sorting**: Provides a linear ordering of vertices in a directed acyclic graph, ensuring that each vertex precedes its neighbors.

These algorithms are crucial for solving various problems related to graphs, from optimizing networks to scheduling tasks based on dependencies. Understanding these concepts will enhance your ability to tackle complex problems in computer science. 
