"""
Given an array of integers, return the index of the first occurrence of a target value. If the target is not found, return -1.
Every time you search for a target value, you can only access the middle element of the current search range. 
If the middle element is equal to the target, return its index. If the middle element is less than the target, 
continue searching in the right half of the array. 
If the middle element is greater than the target, continue searching in the left half of the array.

Time Complexity: O(log n)

Pseudocode:
procedure halfArrSearch(arr : list of integers, target : integer):
    left = 0
    right = length(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        else if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    end while
    return -1
end procedure

"""
def halfArrSearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

