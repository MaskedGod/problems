### 1. **Linear Search**
   - **How it works**: 
     - In a linear search, you go through each element in a list, one by one, until you find the target or reach the end.
     - **Efficiency**: It works for both unsorted and sorted arrays but can be slow because you might need to check every element (O(n) time complexity).
   
   - **Example** (finding 8 in `[3, 5, 8, 1]`):
     - Start with 3 → not 8.
     - Check 5 → not 8.
     - Check 8 → found!

   **Python Code**:
   ```python
   def linear_search(arr, target):
       for i in range(len(arr)):
           if arr[i] == target:
               return i  # Return the index where the target is found
       return -1  # Return -1 if the target is not found

   # Example
   result = linear_search([3, 5, 8, 1], 8)
   print(result)  # Output: 2 (since 8 is at index 2)
   ```

---

### 2. **Binary Search**
   - **How it works**:
     - Binary search works on **sorted arrays**. You repeatedly divide the list in half and compare the target with the middle element.
     - If the target is smaller, you search in the left half; if larger, search in the right half. You keep doing this until the target is found or you run out of elements.
     - **Efficiency**: Much faster than linear search for large, sorted arrays (O(log n) time complexity).

   - **Example** (finding 8 in `[1, 3, 5, 8, 12, 15]`):
     - Middle of the array is 5. Target is 8, so check the right half.
     - Middle of the right half is 12. Target is smaller, so check the left half.
     - Middle of that half is 8 → found!

   **Python Code**:
   ```python
   def binary_search(arr, target):
       low = 0
       high = len(arr) - 1

       while low <= high:
           mid = (low + high) // 2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               low = mid + 1
           else:
               high = mid - 1

       return -1  # Target not found

   # Example
   result = binary_search([1, 3, 5, 8, 12, 15], 8)
   print(result)  # Output: 3 (since 8 is at index 3)
   ```

---

### 3. **Depth-First Search (DFS)**
   - **How it works**:
     - DFS is used to explore nodes in a graph or tree by going as **deep** as possible along one branch before backtracking.
     - It uses a **stack** (or recursion) to keep track of which nodes to explore next.
     - **Efficiency**: DFS can explore large graphs efficiently, but for some graphs, it can get stuck in loops (O(V + E), where V is vertices and E is edges).

   - **Example**: 
     - Start at node A. Visit A → move to a neighbor (say B) → move deeper to B's neighbor (say C) → backtrack when no more neighbors.

   **Python Code (for a graph)**:
   ```python
   def dfs(graph, start, visited=None):
       if visited is None:
           visited = set()

       visited.add(start)
       print(start)  # Visit the node

       for neighbor in graph[start]:
           if neighbor not in visited:
               dfs(graph, neighbor, visited)

   # Example graph (dictionary format)
   graph = {
       'A': ['B', 'C'],
       'B': ['D', 'E'],
       'C': ['F'],
       'D': [],
       'E': [],
       'F': []
   }

   dfs(graph, 'A')
   # Output: A B D E C F (visits each node)
   ```

---

### 4. **Breadth-First Search (BFS)**
   - **How it works**:
     - BFS explores a graph or tree **level by level**. It starts at the root and visits all neighbors at the current level before moving on to the next level.
     - It uses a **queue** to keep track of nodes to visit next.
     - **Efficiency**: BFS is good for finding the shortest path in unweighted graphs (O(V + E) time complexity).

   - **Example**: 
     - Start at node A. Visit A → visit its neighbors B and C → visit B's neighbors D and E → visit C's neighbor F.

   **Python Code (for a graph)**:
   ```python
   from collections import deque

   def bfs(graph, start):
       visited = set()
       queue = deque([start])

       while queue:
           node = queue.popleft()
           if node not in visited:
               print(node)  # Visit the node
               visited.add(node)
               queue.extend(graph[node])  # Add neighbors to the queue

   # Example graph (dictionary format)
   graph = {
       'A': ['B', 'C'],
       'B': ['D', 'E'],
       'C': ['F'],
       'D': [],
       'E': [],
       'F': []
   }

   bfs(graph, 'A')
   # Output: A B C D E F (visits each node level by level)
   ```

---

### Summary of Searching Algorithms:
1. **Linear Search**: Check each element one by one.
2. **Binary Search**: Efficiently splits a sorted array in half to find the target.
3. **Depth-First Search (DFS)**: Goes deep down one path in a graph or tree before backtracking.
4. **Breadth-First Search (BFS)**: Explores each level of a graph or tree before moving to the next.
