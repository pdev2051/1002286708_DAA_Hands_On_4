import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    
    
    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(min_heap, (arrays[i][0], i, 0))
    
    result = []
    
    while min_heap:
        value, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(value)
        
        
        if elem_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(min_heap, (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))
    
    return result


def get_input():
    K = int(input("Enter the number of sorted arrays (K): "))
    arrays = []
    
    for i in range(K):
        N = int(input(f"Enter the size of sorted array {i+1}: "))
        arr = list(map(int, input(f"Enter {N} sorted elements for array {i+1}: ").split()))
        arrays.append(arr)
    
    return arrays

arrays = get_input()
result = merge_k_sorted_arrays(arrays)
print("Merged sorted array:", result)
