### 1. **Bubble Sort**
   - **How it works**: Imagine sorting a list of items by walking down the line and comparing two at a time. If one is bigger than the other, you swap them. Repeat this until no more swaps are needed.
   - **Example with numbers**: 
     - Start: [5, 3, 8, 1]
     - Compare 5 and 3 → Swap: [3, 5, 8, 1]
     - Compare 5 and 8 → No swap.
     - Compare 8 and 1 → Swap: [3, 5, 1, 8]
     - Repeat until sorted: [1, 3, 5, 8]

   **Python Code**:
   ```python
   def bubble_sort(arr):
       n = len(arr)
       for i in range(n):
           for j in range(0, n-i-1):
               if arr[j] > arr[j+1]:
                   # Swap if the element is greater than the next
                   arr[j], arr[j+1] = arr[j+1], arr[j]
       return arr

   # Example
   print(bubble_sort([5, 3, 8, 1]))  # Output: [1, 3, 5, 8]
   ```

---

### 2. **Selection Sort**
   - **How it works**: Imagine finding the smallest item from a group and putting it in its correct spot at the front. Then repeat this process with the rest of the list.
   - **Example**:
     - Start: [5, 3, 8, 1]
     - Find smallest (1), swap with first: [1, 3, 8, 5]
     - Find next smallest (3), already in place.
     - Find next smallest (5), swap with 8: [1, 3, 5, 8]

   **Python Code**:
   ```python
   def selection_sort(arr):
       n = len(arr)
       for i in range(n):
           min_idx = i
           for j in range(i+1, n):
               if arr[j] < arr[min_idx]:
                   min_idx = j
           arr[i], arr[min_idx] = arr[min_idx], arr[i]
       return arr

   # Example
   print(selection_sort([5, 3, 8, 1]))  # Output: [1, 3, 5, 8]
   ```

---

### 3. **Insertion Sort**
   - **How it works**: Like when you sort cards in your hand. You take one card at a time and place it where it belongs among the sorted ones. You keep adding cards to the sorted group.
   - **Example**:
     - Start: [5, 3, 8, 1]
     - Take 5, already sorted.
     - Take 3, place before 5: [3, 5, 8, 1]
     - Take 8, place after 5.
     - Take 1, place before 3: [1, 3, 5, 8]

   **Python Code**:
   ```python
   def insertion_sort(arr):
       for i in range(1, len(arr)):
           key = arr[i]
           j = i - 1
           while j >= 0 and key < arr[j]:
               arr[j + 1] = arr[j]
               j -= 1
           arr[j + 1] = key
       return arr

   # Example
   print(insertion_sort([5, 3, 8, 1]))  # Output: [1, 3, 5, 8]
   ```

---

### 4. **Merge Sort**
   - **How it works**: You keep splitting the list in half until you have single elements. Then, you merge them back together, always keeping the merged halves sorted.
   - **Example**:
     - Start: [5, 3, 8, 1]
     - Split: [5, 3], [8, 1]
     - Split again: [5], [3], [8], [1]
     - Merge sorted pairs: [3, 5], [1, 8]
     - Merge all: [1, 3, 5, 8]

   **Python Code**:
   ```python
   def merge_sort(arr):
       if len(arr) > 1:
           mid = len(arr) // 2
           left_half = arr[:mid]
           right_half = arr[mid:]

           merge_sort(left_half)
           merge_sort(right_half)

           i = j = k = 0

           while i < len(left_half) and j < len(right_half):
               if left_half[i] < right_half[j]:
                   arr[k] = left_half[i]
                   i += 1
               else:
                   arr[k] = right_half[j]
                   j += 1
               k += 1

           while i < len(left_half):
               arr[k] = left_half[i]
               i += 1
               k += 1

           while j < len(right_half):
               arr[k] = right_half[j]
               j += 1
               k += 1

       return arr

   # Example
   print(merge_sort([5, 3, 8, 1]))  # Output: [1, 3, 5, 8]
   ```

---

### 5. **Quick Sort**
   - **How it works**: Pick a "pivot" (like picking a number in the middle of a list). Sort everything smaller than the pivot to the left, and everything larger to the right. Repeat the process for the left and right sides until sorted.
   - **Example**:
     - Start: [5, 3, 8, 1]
     - Pick pivot (say 5), rearrange: [3, 1], 5, [8]
     - Sort left: [1, 3], sort right: [8]
     - Final sorted: [1, 3, 5, 8]

   **Python Code**:
   ```python
   def quick_sort(arr):
       if len(arr) <= 1:
           return arr
       pivot = arr[len(arr) // 2]
       left = [x for x in arr if x < pivot]
       middle = [x for x in arr if x == pivot]
       right = [x for x in arr if x > pivot]
       return quick_sort(left) + middle + quick_sort(right)

   # Example
   print(quick_sort([5, 3, 8, 1]))  # Output: [1, 3, 5, 8]
   ```

---

### 6. **Heap Sort**
   - **How it works**: You build a heap, where each parent is bigger than its children (in max-heap). You remove the largest element (root) and rebuild the heap, shrinking the list as you go.
   - **Example**:
     - Start: [5, 3, 8, 1]
     - Build heap: [8, 3, 5, 1]
     - Remove the largest (8), place at the end, repeat until sorted: [1, 3, 5, 8]

   **Python Code**:
   ```python
   def heapify(arr, n, i):
       largest = i
       left = 2 * i + 1
       right = 2 * i + 2

       if left < n and arr[left] > arr[largest]:
           largest = left

       if right < n and arr[right] > arr[largest]:
           largest = right

       if largest != i:
           arr[i], arr[largest] = arr[largest], arr[i]
           heapify(arr, n, largest)

   def heap_sort(arr):
       n = len(arr)

       for i in range(n // 2 - 1, -1, -1):
           heapify(arr, n, i)

       for i in range(n-1, 0, -1):
           arr[i], arr[0] = arr[0], arr[i]
           heapify(arr, i, 0)

       return arr

   # Example
   print(heap_sort([5, 3, 8, 1]))  # Output: [1, 3, 5, 8]
   ```