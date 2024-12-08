### What are **String Algorithms**?
String algorithms are designed to manipulate, search, and analyze strings. These algorithms are essential in various applications, such as searching for substrings, pattern matching, and text processing.

---

### 1. **KMP Algorithm (Knuth-Morris-Pratt)**
   - **How it works**:
     - The KMP algorithm efficiently searches for occurrences of a "pattern" string within a "text" string. It preprocesses the pattern to create a partial match table (also known as the prefix table) that helps skip unnecessary comparisons.
     - When a mismatch occurs, the algorithm uses the prefix table to determine the next positions to compare, allowing it to avoid re-evaluating characters that have already been matched.

   - **Example Explanation**:
     - Suppose we want to find the pattern "ABABC" in the text "ABABCDABABCDABABC". The KMP algorithm uses the prefix table to skip certain comparisons after mismatches.

   **Python Code**:
   ```python
   def kmp_pattern_search(text, pattern):
       # Preprocess the pattern to create the prefix table
       m, n = len(pattern), len(text)
       lps = [0] * m  # Longest prefix suffix
       j = 0  # Length of previous longest prefix suffix

       # Preprocessing the pattern
       i = 1
       while i < m:
           if pattern[i] == pattern[j]:
               j += 1
               lps[i] = j
               i += 1
           else:
               if j != 0:
                   j = lps[j - 1]
               else:
                   lps[i] = 0
                   i += 1

       # Start searching for the pattern in the text
       i = 0  # Index for text
       j = 0  # Index for pattern
       results = []

       while i < n:
           if pattern[j] == text[i]:
               i += 1
               j += 1

           if j == m:  # A match is found
               results.append(i - j)
               j = lps[j - 1]
           elif i < n and pattern[j] != text[i]:  # Mismatch after j matches
               if j != 0:
                   j = lps[j - 1]
               else:
                   i += 1

       return results

   # Example usage
   text = "ABABCDABABCDABABC"
   pattern = "ABABC"
   matches = kmp_pattern_search(text, pattern)
   print("Pattern found at indices:", matches)
   ```

---

### 2. **Rabin-Karp Algorithm**
   - **How it works**:
     - The Rabin-Karp algorithm uses a hashing technique to search for a pattern in a text. It calculates a hash value for the pattern and for each substring of the text of the same length. If the hash values match, it performs a direct comparison to check for a match.
     - This algorithm is particularly efficient when searching for multiple patterns in the same text.

   - **Example Explanation**:
     - To find the pattern "abc" in the text "abcpqrabcxyz", the algorithm computes the hash for "abc" and compares it with the hash of each substring of length 3 in the text.

   **Python Code**:
   ```python
   def rabin_karp(text, pattern):
       d = 256  # Number of characters in the input alphabet
       q = 101  # A prime number
       m = len(pattern)
       n = len(text)
       p = 0  # Hash value for pattern
       t = 0  # Hash value for text
       h = 1
       results = []

       # The value of h would be "pow(d, m-1)%q"
       for i in range(m - 1):
           h = (h * d) % q

       # Calculate the hash value of pattern and first window of text
       for i in range(m):
           p = (d * p + ord(pattern[i])) % q
           t = (d * t + ord(text[i])) % q

       # Slide the pattern over text
       for i in range(n - m + 1):
           if p == t:  # Check for match
               # Check for characters one by one
               if text[i:i + m] == pattern:
                   results.append(i)

           # Calculate hash value for the next window of text
           if i < n - m:
               t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
               # We might get negative value of t, converting it to positive
               if t < 0:
                   t += q

       return results

   # Example usage
   text = "abcpqrabcxyz"
   pattern = "abc"
   matches = rabin_karp(text, pattern)
   print("Pattern found at indices:", matches)
   ```

---

### 3. **Trie Data Structure**
   - **How it works**:
     - A Trie (pronounced "try") is a tree-like data structure used to efficiently store a dynamic set of strings, particularly useful for searching and prefix matching.
     - Each node represents a character of a string, and the path from the root to a node represents a prefix of strings stored in the Trie. It allows for efficient insertion, deletion, and search operations.

   - **Example Explanation**:
     - If we insert the words "cat", "car", and "dog" into a Trie, the structure will reflect the common prefixes.

   **Python Code**:
   ```python
   class TrieNode:
       def __init__(self):
           self.children = {}
           self.is_end_of_word = False

   class Trie:
       def __init__(self):
           self.root = TrieNode()

       def insert(self, word):
           node = self.root
           for char in word:
               if char not in node.children:
                   node.children[char] = TrieNode()
               node = node.children[char]
           node.is_end_of_word = True

       def search(self, word):
           node = self.root
           for char in word:
               if char not in node.children:
                   return False
               node = node.children[char]
           return node.is_end_of_word

       def starts_with(self, prefix):
           node = self.root
           for char in prefix:
               if char not in node.children:
                   return False
               node = node.children[char]
           return True

   # Example usage
   trie = Trie()
   trie.insert("cat")
   trie.insert("car")
   trie.insert("dog")

   print("Searching 'cat':", trie.search("cat"))  # True
   print("Searching 'car':", trie.search("car"))  # True
   print("Searching 'c':", trie.starts_with("c"))  # True
   print("Searching 'dog':", trie.search("dog"))  # True
   print("Searching 'do':", trie.starts_with("do"))  # True
   print("Searching 'bat':", trie.search("bat"))  # False
   ```

---

### Summary of **String Algorithms**:
1. **KMP Algorithm**: Efficiently searches for a pattern in a text by preprocessing the pattern to create a prefix table, reducing unnecessary comparisons.
2. **Rabin-Karp Algorithm**: Utilizes hashing to search for a pattern in a text, allowing for efficient substring matching, especially when looking for multiple patterns.
3. **Trie Data Structure**: A tree-like structure used to store strings, allowing for efficient insertion, searching, and prefix matching.

These string algorithms are fundamental in many applications, including text editors, search engines, and auto-complete features. Understanding how they work will help you efficiently handle various string-related problems. 