
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
