def remove_duplicates(arr):
    return list(dict.fromkeys(arr))  # Removes duplicates while maintaining order

def get_input():
    K = int(input("Enter number of arrays: "))
    return [list(map(int, input(f"Enter sorted array {i+1}: ").split())) for i in range(K)]

# Process input and print results
for i, arr in enumerate(get_input(), 1):
    print(f"Output Array {i}: {remove_duplicates(arr)}")
