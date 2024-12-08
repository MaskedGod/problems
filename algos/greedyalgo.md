### What are **Greedy Algorithms**?
Greedy algorithms make a series of choices, each of which looks best at the moment, with the hope of finding a global optimum. They are often used in optimization problems where local optimization leads to a global solution.

### Key Characteristics of Greedy Algorithms:
1. **Local Optimum**: Greedy algorithms choose the best option available at each step without looking ahead.
2. **Irrevocability**: Once a choice is made, it cannot be undone.
3. **Feasibility**: Every choice must be feasible and respect the problem's constraints.

Now, let’s discuss each greedy algorithm in detail.

---

### 1. **Dijkstra’s Algorithm**
   - **How it works**:
     - Dijkstra’s algorithm finds the shortest path from a starting node to all other nodes in a weighted graph with non-negative weights.
     - It maintains a priority queue of vertices to explore, starting from the source vertex and iteratively selecting the closest vertex until all vertices are visited.
     - **Efficiency**: Time complexity is O((V + E) log V), where V is the number of vertices and E is the number of edges.

   - **Example Explanation**:
     - Given a graph where nodes represent cities and edges represent distances between them, Dijkstra's algorithm helps find the shortest route from one city to all others.

   **Python Code**:
   ```python
   import heapq

   def dijkstra(graph, start):
       # Initialize distances with infinity and set the distance to the start node to 0
       distances = {vertex: float('infinity') for vertex in graph}
       distances[start] = 0
       priority_queue = [(0, start)]  # (distance, vertex)

       while priority_queue:
           current_distance, current_vertex = heapq.heappop(priority_queue)

           # If the distance is greater than the recorded distance, skip it
           if current_distance > distances[current_vertex]:
               continue

           for neighbor, weight in graph[current_vertex].items():
               distance = current_distance + weight

               # Only consider this new path if it's better
               if distance < distances[neighbor]:
                   distances[neighbor] = distance
                   heapq.heappush(priority_queue, (distance, neighbor))

       return distances

   # Example graph represented as an adjacency list
   graph = {
       'A': {'B': 1, 'C': 4},
       'B': {'A': 1, 'C': 2, 'D': 5},
       'C': {'A': 4, 'B': 2, 'D': 1},
       'D': {'B': 5, 'C': 1},
   }
   print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
   ```

---

### 2. **Prim’s Algorithm**
   - **How it works**:
     - Prim’s algorithm finds the minimum spanning tree (MST) for a connected, undirected graph with weighted edges.
     - It starts from an arbitrary vertex and grows the MST by adding the smallest edge connecting the tree to a vertex not already in the tree.
     - **Efficiency**: Time complexity is O(E log V) using a priority queue.

   - **Example Explanation**:
     - If you have a network of cities connected by roads with different construction costs, Prim's algorithm helps determine the minimum cost to connect all cities.

   **Python Code**:
   ```python
   import heapq

   def prim(graph):
       start_vertex = next(iter(graph))  # Start from an arbitrary vertex
       mst = []
       visited = {start_vertex}
       edges = [
           (cost, start_vertex, to)
           for to, cost in graph[start_vertex].items()
       ]
       heapq.heapify(edges)  # Create a priority queue of edges

       while edges:
           cost, frm, to = heapq.heappop(edges)  # Get the smallest edge
           if to not in visited:
               visited.add(to)
               mst.append((frm, to, cost))  # Add to the MST

               for next_to, next_cost in graph[to].items():
                   if next_to not in visited:
                       heapq.heappush(edges, (next_cost, to, next_to))

       return mst

   # Example graph represented as an adjacency list
   graph = {
       'A': {'B': 1, 'C': 4},
       'B': {'A': 1, 'C': 2, 'D': 5},
       'C': {'A': 4, 'B': 2, 'D': 1},
       'D': {'B': 5, 'C': 1},
   }
   print(prim(graph))  # Output: [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 1)]
   ```

---

### 3. **Huffman Encoding**
   - **How it works**:
     - Huffman encoding is a lossless data compression algorithm that uses variable-length codes to represent characters based on their frequencies. More frequent characters get shorter codes, while less frequent characters get longer codes.
     - It builds a binary tree where each leaf node represents a character. The path from the root to the leaf node represents the character's code.
     - **Efficiency**: The average time complexity is O(n log n), where n is the number of unique characters.

   - **Example Explanation**:
     - Suppose you want to compress the string `"banana"`. The character frequencies are `{'b': 1, 'a': 3, 'n': 2}`. Huffman encoding assigns shorter codes to more frequent characters to reduce the total size.

   **Python Code**:
   ```python
   from collections import Counter, defaultdict
   import heapq

   class Node:
       def __init__(self, char, freq):
           self.char = char
           self.freq = freq
           self.left = None
           self.right = None

       def __lt__(self, other):
           return self.freq < other.freq

   def huffman_encoding(data):
       if not data:
           return "", {}

       frequency = Counter(data)
       priority_queue = [Node(char, freq) for char, freq in frequency.items()]
       heapq.heapify(priority_queue)

       while len(priority_queue) > 1:
           left = heapq.heappop(priority_queue)
           right = heapq.heappop(priority_queue)
           merged = Node(None, left.freq + right.freq)
           merged.left = left
           merged.right = right
           heapq.heappush(priority_queue, merged)

       root = priority_queue[0]
       huffman_code = {}

       def generate_codes(node, code):
           if node:
               if node.char is not None:  # It's a leaf node
                   huffman_code[node.char] = code
               generate_codes(node.left, code + "0")
               generate_codes(node.right, code + "1")

       generate_codes(root, "")
       encoded_data = ''.join(huffman_code[char] for char in data)

       return encoded_data, huffman_code

   # Example
   data = "banana"
   encoded, code_map = huffman_encoding(data)
   print("Encoded data:", encoded)
   print("Huffman Codes:", code_map)
   ```

---

### Summary of **Greedy Algorithms**:
1. **Dijkstra’s Algorithm**: Efficiently finds the shortest path from a source vertex to all others in a graph with non-negative weights.
2. **Prim’s Algorithm**: Constructs the minimum spanning tree of a graph by growing it from an arbitrary starting vertex.
3. **Huffman Encoding**: Compresses data by assigning variable-length codes based on character frequencies, achieving efficient storage.

These algorithms illustrate how greedy choices can lead to optimal solutions for specific types of problems. Understanding these techniques will help you tackle various optimization and graph-related challenges.
