"""
Linear Search Algorithm 

Time Complexity: O(n)
Space Complexity: O(1)

Pseudocode:
procedure linearSearch(arr : list of elements, target : element):
    for i = 0 to length(arr) - 1:
        if arr[i] == target:
            return i
    end for
    return -1
end procedure
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

nasa_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = linear_search(nasa_lista, target)
if result != -1:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in the list")