
# Time Complexity Analysis of the Algorithm - Merged Arrays
The algorithm uses a min-heap (priority queue) to efficiently merge K sorted arrays of size N each. Let's analyze the time complexity step by step.

# Initializing the Min-Heap
We insert the first element of each of the K arrays into the min-heap.
Each insertion into the min-heap takes O(log K) time.
Since we insert K elements initially, the total time for this step is:
O(K log K)

# Processing All Elements
The total number of elements across all arrays is N × K.
We extract the smallest element from the heap and insert the next element from the corresponding array.
Extracting the minimum element from a heap takes O(log K).
Inserting a new element into the heap also takes O(log K).
Since we do this operation for each of the N × K elements, the total time for this step is:
O(N Klog K)

# Overall Time Complexity
Adding both steps together:

𝑂(𝐾 log𝐾) + 𝑂(𝑁 𝐾 log𝐾) = 𝑂(𝑁 𝐾log𝐾)
O(KlogK)+O(NKlogK)=O(NKlogK)
Since O(NK \log K) dominates O(K \log K), the final time complexity of the algorithm is:
O(NKlogK)

# Ways to Improve the Implementation
# Use a Min-Heap with a Custom Object (Tuple is Fine but Can Be More Efficient)

Currently, we use a tuple (value, array_index, element_index) in the heap. While Python handles this well, using a lightweight named tuple or a small custom object can slightly optimize memory usage and readability.

# Use Itertools' heapq.merge() for Simplicity

Python provides heapq.merge(), which can merge multiple sorted iterables efficiently.
This eliminates the need to manually push and pop from a heap.

Time Complexity: Still O(NK log K) but with less manual heap management.

# Reduce Heap Size by Merging in Pairs (Divide & Conquer)

Instead of merging all arrays at once, merge them in pairs, reducing the effective heap operations.
Steps:
Merge two arrays at a time.
Push merged arrays back into the heap.
This reduces the number of heap operations and balances the load.
Time Complexity: Still O(NK log K) but improves practical performance.

# Use Multi-threading for Parallel Processing (For Large Inputs)

If K is large, parallelizing the merge process across threads/processes can speed up execution.
Example: Use multiprocessing.Pool to merge sub-arrays in parallel.

# Optimize Heap Operations Using a Binary Index Tree or Fibonacci Heap

While heapq is efficient, Fibonacci heaps offer a faster amortized time complexity for insertions.
This can be useful for extremely large K.




# Time Complexity (Processing All Arrays) - Duplicates Array 
remove_duplicates(arr) Function
dict.fromkeys(arr):
Iterates through the array O(N)
Inserts each unique element into a dictionary (hash table) O(1) per insertion
Total time complexity: O(N)
list(dict.fromkeys(arr)):
Converts the dictionary keys back to a list O(N)
Total time complexity remains O(N)
Overall Complexity of remove_duplicates(arr):
O(N)

# get_input() Function
Takes K arrays as input.
Each input line processes O(N)
Since there are K arrays, total complexity:
O(KN)
We process K arrays, each with an O(N) operation.
Overall time complexity:
O(KN)

# Final Complexity (Processing All Arrays)
We process K arrays, each with an O(N) operation.
Overall time complexity:
O(KN)


# Ways to Improve the Implementation 
1. Use a Two-Pointer Approach (In-Place Modification)
Instead of using dict.fromkeys(), modify the array in place to save space.

Improvements: ✅ Time Complexity: Still O(N)
✅ Space Complexity: Now O(1) instead of O(N)

#  Use itertools.groupby() for Cleaner Code
Python’s itertools.groupby() can group consecutive duplicates efficiently.

# Pros:

Cleaner and more Pythonic
Still O(N) time complexity
Saves space (O(1) extra space)
